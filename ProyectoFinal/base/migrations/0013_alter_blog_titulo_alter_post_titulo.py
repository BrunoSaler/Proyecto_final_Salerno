# Generated by Django 5.0 on 2023-12-16 19:39

import base.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_blog_fecha_alter_comentario_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=base.models.UpperField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=base.models.UpperField(max_length=100, unique=True),
        ),
    ]
