# Generated by Django 3.0.5 on 2020-04-05 11:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20200326_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
