# Generated by Django 5.0.7 on 2024-07-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_service_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
