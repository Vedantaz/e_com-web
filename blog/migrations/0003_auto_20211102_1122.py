# Generated by Django 3.2.7 on 2021-11-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211031_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='Thumbemail',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='thumbemail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
