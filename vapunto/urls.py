from mimetypes import init
from django.urls import path

from vapunto import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('port', views.port, name='port'),
    path('product', views.product, name='product'),
    path('modproducto/<int:prod_actual>', views.modproducto, name="modproducto"),
    path('borrproducto/<int:prod_actual>', views.borrproducto, name="borrproducto"),
    path('salir', views.salir, name='salir'),
    path('verusuario', views.verusuario, name='verusuario'),
    path('modusuario/<int:usu_actual>',  views.modusuario, name='modusuario'),
    path('borusuario/<int:usu_actual>', views.borusuario, name='borusuario'),
    path('vercliente', views.vercliente, name='vercliente'),
    path('modcliente/<int:cli_actual>', views.modcliente, name="modcliente"),
    path('borcliente/<int:cli_actual>', views.borcliente, name="borcliente"),
    path('proveedor', views.proveedor, name='proveedor'),
    path('modprovee/<int:pro_actual>', views.modprovee, name="modprovee"),
    path('borprovee/<int:pro_actual>', views.borprovee, name="borprovee"),
    path('pais', views.pais, name='pais'),
    path('modpais/<int:pai_actual>', views.modpais, name="modpais"),
    path('borpais/<int:pai_actual>', views.borpais, name="borpais"),
    path('ciudad', views.ciudad, name='ciudad'),
    path('modciudad/<int:ciu_actual>', views.modciudad, name="modciudad"),
    path('borciudad/<int:ciu_actual>', views.borciudad, name="borciudad"),
    path('fondos/<int:caja_actual>', views.fondos, name='fondos'),
    path('Auditoria', views.audirep, name='Auditoria'),
    path('venta', views.venta, name='venta'),
    path('venta_detalle', views.venta_detalle, name='venta_detalle'),
    path('r_venta', views.registro, name='r_venta'),
    path(r'registro/<int:sale_id>', views.detailprod, name='detailprod')
]
