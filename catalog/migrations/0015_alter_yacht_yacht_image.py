# Generated by Django 4.1.7 on 2023-04-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_yacht_yacht_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yacht',
            name='yacht_image',
            field=models.ManyToManyField(related_name='yachts', to='catalog.image'),
        ),
    ]
