# Generated by Django 4.1.5 on 2023-03-16 21:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=24, verbose_name='Name')),
                ('body', models.CharField(db_index=True, max_length=216, verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('likes', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Likes')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
