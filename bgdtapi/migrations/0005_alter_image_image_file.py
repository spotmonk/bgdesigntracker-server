# Generated by Django 3.2.5 on 2021-07-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgdtapi', '0004_rename_user_id_bgdtuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.FileField(upload_to='static/pics/'),
        ),
    ]
