# Generated by Django 4.1.7 on 2023-03-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_specifications_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specifications',
            name='cruising_speed',
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text='Cruising speed in kn.',
                max_digits=3,
                null=True),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='length_overall',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text='LOA in ft.',
                max_digits=5,
                null=True),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='max_speed',
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text='Maximum speed in kn.',
                max_digits=3,
                null=True),
        ),
    ]
