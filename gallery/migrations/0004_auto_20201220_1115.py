# Generated by Django 3.1.4 on 2020-12-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(null=True, upload_to='pictures/'),
        ),
    ]