# Generated by Django 3.1.2 on 2020-10-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0005_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='', upload_to='product_images/'),
        ),
    ]
