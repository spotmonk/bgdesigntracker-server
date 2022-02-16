from rest_framework import viewsets, parsers
from bgdtapi.models import Image
from bgdtapi.serializers import ImageSerializer
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ImageViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser]  
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(methods=['post'], detail=False, permission_classes=[] )
    def profile(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)