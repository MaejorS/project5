# Generated by Django 5.2.1 on 2025-05-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image_url_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, help_text='Paste a Cloudinaryimage URL here if not uploading.', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage_gb',
            field=models.PositiveIntegerField(help_text='Enter storage in GB'),
        ),
    ]
