# Generated by Django 3.2.7 on 2022-01-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0011_auto_20220113_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.proveedor'),
        ),
    ]
