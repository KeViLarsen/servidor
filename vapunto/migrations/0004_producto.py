# Generated by Django 3.2.7 on 2021-11-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0003_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codigo_productos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_productos', models.CharField(max_length=50)),
                ('preciocompra_productos', models.IntegerField()),
                ('precioventa_productos', models.IntegerField()),
                ('categoria_productos', models.CharField(max_length=50)),
                ('cantidad_productos', models.IntegerField()),
            ],
        ),
    ]
