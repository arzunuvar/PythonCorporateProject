# Generated by Django 3.0.5 on 2020-05-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucontent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]