# Generated by Django 3.2.7 on 2022-02-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0005_caja_total_caja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='entrada_caja',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='salida_caja',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
