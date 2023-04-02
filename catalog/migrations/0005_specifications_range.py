# Generated by Django 4.1.7 on 2023-03-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_propulsion_engine_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specifications',
            name='range',
            field=models.PositiveIntegerField(blank=True, help_text='The max. distance that the yacht can travel from the shore in nm.', null=True),
        ),
    ]