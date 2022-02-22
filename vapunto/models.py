
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey

from datetime import datetime


# Create your models here.

   
class Usuariosid(models.Model):
    codigo_usuario = models.AutoField(primary_key = True)
    nombre_usuario = models.CharField(max_length = 50)
    password_usuario = models.CharField(max_length = 50)
    nombre_completo_usuario = models.CharField(max_length = 200)
    tipo_usuario=models.IntegerField()

class Nacionalidad(models.Model):
    codigo_nacionalidad = models.AutoField(primary_key = True)
    nacionalidad = models.CharField(max_length = 50)

class Ciudad(models.Model):
    codigo_ciudad = models.AutoField(primary_key = True)
    ciudad = models.CharField(max_length = 50)

class Proveedor(models.Model):
    codigo_proveedor=models.AutoField(primary_key=True)
    nombre_proveedor= models.CharField(max_length = 50)
    ruc_proveedor= models.IntegerField()
    telefono_proveedor= models.IntegerField()
    nacionalidad = models.ForeignKey(Nacionalidad ,on_delete=models.CASCADE,null=True)
    ciudad = models.ForeignKey(Ciudad ,on_delete=models.CASCADE,null=True)

class producto(models.Model):
    codigo_productos=models.IntegerField(primary_key=True)
    nombre_productos= models.CharField(max_length = 50)
    preciocompra_productos= models.DecimalField(max_digits=9, decimal_places=2)
    precioventa_productos= models.DecimalField( max_digits=9, decimal_places=2)
    categoria_productos= models.CharField(max_length = 50)
    cantidad_productos=models.IntegerField()
    fecha_productos=models.DateField()
    nombre_proveedor = models.ForeignKey(Proveedor ,on_delete=models.CASCADE,null=True)


class Clientes(models.Model):
    codigo_cliente = models.AutoField(primary_key = True)
    ruc_cliente = models.CharField(max_length = 50)
    nombre_cliente = models.CharField(max_length = 50)
    apellido_cliente = models.CharField(max_length = 50)
    telefono_cliente = models.CharField(max_length = 200)
    nacionalidad = models.ForeignKey(Nacionalidad ,on_delete=models.CASCADE,null=True)
    ciudad = models.ForeignKey(Ciudad ,on_delete=models.CASCADE,null=True)

class Clientes2(models.Model):
    codigo_cliente = models.IntegerField(primary_key=True)
    ruc_cliente = models.CharField(max_length = 50)
    nombre_cliente = models.CharField(max_length = 50)
    apellido_cliente = models.CharField(max_length = 50)
    telefono_cliente = models.CharField(max_length = 200)
    nacionalidad = models.ForeignKey(Nacionalidad ,on_delete=models.CASCADE,null=True)
    ciudad = models.ForeignKey(Ciudad ,on_delete=models.CASCADE,null=True)
    codigo_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length = 50)

class producto2(models.Model):
    codigo_productos=models.IntegerField(primary_key=True)
    nombre_productos= models.CharField(max_length = 50)
    preciocompra_productos= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precioventa_productos= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    categoria_productos= models.CharField(max_length = 50)
    cantidad_productos=models.IntegerField()
    fecha_productos=models.DateField()
    nombre_proveedor = models.ForeignKey(Proveedor ,on_delete=models.CASCADE,null=True)
    codigo_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length = 50)

class Proveedor2(models.Model):
    codigo_proveedor=models.IntegerField(primary_key=True)
    nombre_proveedor= models.CharField(max_length = 50)
    ruc_proveedor= models.IntegerField()
    telefono_proveedor= models.IntegerField()
    nacionalidad = models.ForeignKey(Nacionalidad ,on_delete=models.CASCADE,null=True)
    ciudad = models.ForeignKey(Ciudad ,on_delete=models.CASCADE,null=True)
    codigo_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length = 50)

class Nacionalidad2(models.Model):
    codigo_nacionalidad = models.IntegerField(primary_key=True)
    nacionalidad = models.CharField(max_length = 50)
    codigo_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length = 50)

class Ciudad2(models.Model):
    codigo_ciudad = models.IntegerField(primary_key=True)
    ciudad = models.CharField(max_length = 50)
    codigo_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length = 50)

class Caja(models.Model):
    codigo_caja = models.AutoField(primary_key=True)
    fecha_caja = models.DateField()
    hora_caja = models.TimeField()
    motivo_caja = models.CharField(max_length = 50, null=True)
    entrada_caja = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,null=True)
    salida_caja = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,null=True)
    tipo_mov=models.IntegerField(null=True)
    total_caja = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=True)
    codigo_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length = 50)

class MethodPay(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)


class Sale(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    cli = models.ForeignKey(Clientes ,on_delete=models.CASCADE,null=True)
    date_joined = models.DateField(default=datetime.now)
    pay = models.ForeignKey(MethodPay ,on_delete=models.CASCADE,null=True)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

class Order (models.Model):
    order_id = models.AutoField(primary_key=True)
    orden = models.IntegerField(null=True)
    sale_id = models.ForeignKey(Sale ,on_delete=models.CASCADE,null=True)
    codigo_producto = models.IntegerField()
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField()
    

class DetSale(models.Model):
    sale = models.IntegerField()
    prod = models.ForeignKey(producto, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField()
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
  