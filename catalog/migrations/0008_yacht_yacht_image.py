# Generated by Django 4.1.7 on 2023-03-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_specifications_twin_berths'),
    ]

    operations = [
        migrations.AddField(
            model_name='yacht',
            name='yacht_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
