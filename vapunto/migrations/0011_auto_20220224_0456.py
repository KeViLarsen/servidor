# Generated by Django 3.2.7 on 2022-02-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0010_alter_caja_hora_caja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='monto_caja',
        ),
        migrations.AddField(
            model_name='caja',
            name='entrada_caja',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='caja',
            name='salida_caja',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True),
        ),
    ]