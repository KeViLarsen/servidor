# Generated by Django 3.2.7 on 2022-02-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0003_auto_20220218_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes2',
            name='codigo_cliente',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
