import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from jwt.exceptions import InvalidSignatureError
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from bgdtapi.models import BGDTUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import requests
import env
import jwt

@csrf_exempt
@api_view(['POST', ])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode('utf-8'))
    print(req_body)
    try: 
        decoded = jwt.decode(req_body["token"], env.SUPATOKEN, algorithms="HS256", audience="authenticated")
    
    except InvalidSignatureError:
        print("token does not match")
        data = json.dumps({"valid": False})
        return HttpResponse(data, content_type='application/json')
    else:
        password = env.DEFAULT_PASSWORD
    print(decoded)
    try: 
        user = User.objects.get(username=decoded["sub"])
    # If authentication was successful, respond with their token
        BGDTuser = BGDTUser.objects.get(user_id=user)
        token = Token.objects.get(user=user)
        data = json.dumps({"valid": True, "token": token.key, "user_id": BGDTuser.id})
        return HttpResponse(data, content_type='application/json')
    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
   
    except User.DoesNotExist: 
        new_user = User.objects.create_user(
            username=decoded['sub'],
            email=decoded['email'],
            password=password
        )

        BGDTuser = BGDTUser.objects.create(
            bio='',
            profile_image_url='',
            user=new_user
        )

        # Commit the user to the database by saving it
        BGDTuser.save()

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=new_user)

        # Return the token to the client
        data = json.dumps({"valid": True, "token": token.key, "user_id": BGDTuser.id})
        return HttpResponse(data, content_type='application/json')