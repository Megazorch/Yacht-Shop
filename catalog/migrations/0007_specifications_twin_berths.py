# Generated by Django 4.1.7 on 2023-03-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_specifications_cruising_speed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specifications',
            name='twin_berths',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]