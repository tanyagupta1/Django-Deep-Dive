# Generated by Django 4.1.2 on 2022-10-27 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_patient_fullname_alter_patient_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_verified',
            new_name='user_type_decided',
        ),
    ]
