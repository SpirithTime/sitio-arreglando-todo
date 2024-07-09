# Generated by Django 5.0.6 on 2024-07-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='add_producto'),
        ),
    ]
