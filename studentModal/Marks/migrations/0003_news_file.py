# Generated by Django 2.2.3 on 2019-11-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marks', '0002_auto_20191123_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
