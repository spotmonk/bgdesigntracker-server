# Generated by Django 3.2.5 on 2021-07-24 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgdtapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bgdtuser',
            old_name='user_id',
            new_name='userid',
        ),
    ]
