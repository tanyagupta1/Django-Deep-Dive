# Generated by Django 4.1.2 on 2022-10-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.CharField(default='Delhi', max_length=200, null=True),
        ),
    ]
