# Generated by Django 5.0.6 on 2024-07-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
    ]
