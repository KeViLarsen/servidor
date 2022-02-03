# Generated by Django 3.2.7 on 2022-02-03 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad2',
            fields=[
                ('codigo_ciudad', models.IntegerField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=50)),
                ('codigo_usuario', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('codigo_nacionalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad2',
            fields=[
                ('codigo_nacionalidad', models.IntegerField(primary_key=True, serialize=False)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('codigo_usuario', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuariosid',
            fields=[
                ('codigo_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('password_usuario', models.CharField(max_length=50)),
                ('nombre_completo_usuario', models.CharField(max_length=200)),
                ('tipo_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor2',
            fields=[
                ('codigo_proveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('ruc_proveedor', models.IntegerField()),
                ('telefono_proveedor', models.IntegerField()),
                ('codigo_usuario', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.ciudad')),
                ('nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('codigo_proveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('ruc_proveedor', models.IntegerField()),
                ('telefono_proveedor', models.IntegerField()),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.ciudad')),
                ('nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='producto2',
            fields=[
                ('codigo_productos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_productos', models.CharField(max_length=50)),
                ('preciocompra_productos', models.IntegerField()),
                ('precioventa_productos', models.IntegerField()),
                ('categoria_productos', models.CharField(max_length=50)),
                ('cantidad_productos', models.IntegerField()),
                ('codigo_usuario', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codigo_productos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_productos', models.CharField(max_length=50)),
                ('preciocompra_productos', models.IntegerField()),
                ('precioventa_productos', models.IntegerField()),
                ('categoria_productos', models.CharField(max_length=50)),
                ('cantidad_productos', models.IntegerField()),
                ('fecha_productos', models.DateField()),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes2',
            fields=[
                ('codigo_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('ruc_cliente', models.CharField(max_length=50)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(max_length=200)),
                ('codigo_usuario', models.IntegerField()),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.ciudad')),
                ('nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('codigo_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('ruc_cliente', models.CharField(max_length=50)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(max_length=200)),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.ciudad')),
                ('nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vapunto.nacionalidad')),
            ],
        ),
    ]
