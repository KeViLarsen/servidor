from gettext import translation
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from vapunto.models import *
from vapunto.models import producto
from vapunto.models import Caja


def login(request):
    if request.method == "GET":
        if request.session.get("codigo_usuario"):
            return redirect("inicio")
        else: 
            return render(request, 'login.html')
    if request.method == "POST":
        nusuario = request.POST.get("Usuario")
        pusuario = request.POST.get("Password")
        usuario_actual=Usuariosid.objects.filter(nombre_usuario=nusuario).exists()
        if usuario_actual:
            datos_usuario=Usuariosid.objects.filter(nombre_usuario=nusuario).first()
            if getattr(datos_usuario,"password_usuario")==pusuario:
                request.session["codigo_usuario"]=getattr(datos_usuario, "codigo_usuario")
                request.session["nombredelusuario"]=getattr(datos_usuario, "nombre_usuario")
                request.session["nombre_completo_usuario"]=getattr(datos_usuario, "nombre_completo_usuario")
                request.session["tipo_usuario"]=getattr(datos_usuario, "tipo_usuario")
                return redirect("inicio")
            else:
                return render(request, 'login.html', {"mensaje_error":"Contraseña ingresada es incorrecta."})
        else:
            return render(request, 'login.html', {"mensaje_error":"Usuario ingresado no existe."})

def inicio(request):
    if request.session.get("codigo_usuario"):
        return validar(request, 'index.html', {"nombre_usuario": request.session.get("nombre_completo_usuario")})
    else:
        return redirect('login')

def salir(request):
    request.session.flush()
    return redirect('./')
    
def tabla(request):
    return validar(request,'tables.html')
  
def product(request):
    if request.session.get("codigo_usuario"):
        listatabla=producto.objects.all()
        listaproveedor=Proveedor.objects.all()
        return validar(request,"produ/product.html",{"listatabla":listatabla,"listaproveedor":listaproveedor})
    else:
         return redirect("login")

def modproducto(request, prod_actual = 0):
    listaproveedor=Proveedor.objects.all()
    listatabla=producto.objects.all()
    if request.session.get("codigo_usuario"):
            if request.method=="GET":
                producto_actual=producto.objects.filter(codigo_productos=prod_actual).exists()
                if producto_actual:
                    datos_producto=producto.objects.filter(codigo_productos=prod_actual).first()
                    datos_producto.fecha_productos=str(datos_producto.fecha_productos)
                    return validar(request, 'produ/modproducto.html',
                    {"datos_act":datos_producto, "prod_actual":prod_actual, "titulo_f":"Editar un Producto","listaproveedor":listaproveedor,"listatabla":listatabla})
                else:
                    return validar(request, "produ/modproducto.html", {"titulo_f":"Nuevo Producto","prod_actual": prod_actual,"listaproveedor":listaproveedor,"listatabla":listatabla})

            if request.method=="POST":
                if prod_actual==0:
                    producto_nuevo=producto(codigo_productos=request.POST.get('codigo'),
                    nombre_productos=request.POST.get("nombre"),
                    preciocompra_productos=request.POST.get("costo"),
                    precioventa_productos=request.POST.get("venta"),
                    categoria_productos=request.POST.get("categoria"),
                    fecha_productos=request.POST.get('fecha'),
                    cantidad_productos=request.POST.get("cantidad"),
                    nombre_proveedor_id=request.POST.get("proveedor")      
                    )
                    producto_nuevo.save()
                else:
                    datos_usuario=producto.objects.filter(codigo_productos=prod_actual).first()
                    producto_nueva=producto2(nombre_productos = datos_usuario.nombre_productos,
                    preciocompra_productos=datos_usuario.preciocompra_productos,
                    codigo_usuario=request.session.get("codigo_usuario"),
                    nombre_usuario=request.session.get("nombre_completo_usuario"),
                    precioventa_productos=datos_usuario.precioventa_productos,
                    categoria_productos=datos_usuario.categoria_productos,
                    cantidad_productos=datos_usuario.cantidad_productos,
                    codigo_productos=datos_usuario.codigo_productos,
                    nombre_proveedor_id=datos_usuario.nombre_proveedor_id,
                    fecha_productos=request.POST.get('fecha'))
                    producto_nueva.save()

                    producto_actual=producto.objects.get(codigo_productos=prod_actual)
                    producto_actual.nombre_productos=request.POST.get("nombre")
                    producto_actual.preciocompra_productos=request.POST.get("costo")
                    producto_actual.precioventa_productos=request.POST.get("venta")
                    producto_actual.categoria_productos=request.POST.get("categoria")
                    producto_actual.fecha_productos=request.POST.get('fecha')
                    producto_actual.cantidad_productos=request.POST.get("cantidad")
                    producto_actual.nombre_proveedor_id=request.POST.get("proveedor")
                    producto_actual.save()

            
            return redirect("../product")
    else:
         return redirect("login")

def borrproducto(request, prod_actual):
        listatabla=producto.objects.all()
        producto.objects.filter(codigo_productos=prod_actual).delete() 
        return render(request,"produ/product.html",{"listatabla":listatabla ,"deletconf":"eliminado"})

def registrar(request):
    return render(request,'register.html')

def modusuario(request,usu_actual=0):
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            usuario_actual=Usuariosid.objects.filter(codigo_usuario=usu_actual).exists()
            if usuario_actual:
                datos_usuario=Usuariosid.objects.filter(codigo_usuario=usu_actual).first()
                return validar(request, "user/modusuario.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_s":"Modificar Usuario", 
                "subtitulo_s":"Vuleva a escribir los datos que desea modificar", 
                "datos_act":datos_usuario, 
                "usu_actual":usu_actual})
            else:
                return validar(request, "user/modusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_s":"Nuevo Usuario", "subtitulo_s":"Por favor complete todos los datos solicitados", "usu_actual":usu_actual})

        if request.method=="POST":
            if usu_actual==0:
                usuario_nuevo=Usuariosid(codigo_usuario=request.POST.get('codigo_usuario'), 
                nombre_usuario=request.POST.get('nombre_usuario'), 
                password_usuario=request.POST.get('password_usuario'), 
                nombre_completo_usuario=request.POST.get('nombre_completo_usuario'), 
                tipo_usuario=request.POST.get('tipo_usuario'))
                usuario_nuevo.save()
            else:
                usuario_actual=Usuariosid.objects.get(codigo_usuario=usu_actual)
                usuario_actual.nombre_usuario=request.POST.get('nombre_usuario')
                usuario_actual.nombre_completo_usuario=request.POST.get('nombre_completo_usuario')
                usuario_actual.password_usuario=request.POST.get('password_usuario')
                usuario_actual.tipo_usuario=request.POST.get('tipo_usuario')
                usuario_actual.save()

        return redirect('../verusuario')
    else:
        return redirect("login")

def verusuario(request):
    if request.session.get("codigo_usuario"):
        listatabla=Usuariosid.objects.all()
        return validar(request, "user/verusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"),
         "titulo_s":"Usuarios", "subtitulo_s":"Listado de Usuarios registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def borusuario(request, usu_actual):
    listatabla=Usuariosid.objects.all()
    Usuariosid.objects.filter(codigo_usuario=usu_actual).delete()
    return render(request,"user/verusuario.html",{"listatabla":listatabla,"deletconf":"eliminado"})

def vercliente(request):
    if request.session.get("codigo_usuario"):
        listatabla=Clientes.objects.all()
        listanacionalidades = Nacionalidad.objects.all()
        listaciudad = Ciudad.objects.all()
        return validar(request,"cliente/vercliente.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})
    else:
         return redirect("login")
    
def modcliente(request, cli_actual = 0):
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            cliente_actual=Clientes.objects.filter(codigo_cliente=cli_actual).exists()
            if cliente_actual:
                datos_cliente=Clientes.objects.filter(codigo_cliente=cli_actual).first()
                return validar(request, 'cliente/modcliente.html',
                {"datos_act":datos_cliente, "cli_actual":cli_actual, "titulo_f":"Editar un Cliente", "listanacionalidades":listanacionalidades, "listaciudad":listaciudad} )
            else:
                return validar(request, "cliente/modcliente.html", {"titulo_f":"Cargar nuevo Cliente","cli_actual": cli_actual, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})

        if request.method=="POST":
            if cli_actual==0:
                cliente_nuevo=Clientes(codigo_cliente=request.POST.get('codigo'),
                nombre_cliente=request.POST.get("nombre"),
                apellido_cliente=request.POST.get("apellido"),
                ruc_cliente=request.POST.get("ruc"),
                telefono_cliente=request.POST.get("telefono"),
                nacionalidad_id=request.POST.get("nacionalidad") ,
                ciudad_id=request.POST.get("ciudad")
                        
                )
                cliente_nuevo.save()
            else:
                datos_usuario=Clientes.objects.filter(codigo_cliente=cli_actual).first()
                cliente_nueva=Clientes2(nombre_cliente = datos_usuario.nombre_cliente,
                ruc_cliente=datos_usuario.ruc_cliente,
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"),
                codigo_cliente=datos_usuario.codigo_cliente,
                apellido_cliente=datos_usuario.apellido_cliente,
                telefono_cliente=datos_usuario.telefono_cliente,
                nacionalidad=datos_usuario.nacionalidad,
                ciudad=datos_usuario.ciudad)
                cliente_nueva.save()
                
                cliente_actual=Clientes.objects.get(codigo_cliente=cli_actual)
                cliente_actual.nombre_cliente=request.POST.get("nombre")
                cliente_actual.apellido_cliente=request.POST.get("apellido")
                cliente_actual.ruc_cliente=request.POST.get("ruc")
                cliente_actual.telefono_cliente=request.POST.get("telefono")
                cliente_actual.nacionalidad_id=request.POST.get("nacionalidad")
                cliente_actual.ciudad_id=request.POST.get("ciudad")
                cliente_actual.save()

        return redirect("../vercliente")
    else:
        return redirect("login")
        
def borcliente(request, cli_actual):
    listatabla=Clientes.objects.all()
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    Clientes.objects.filter(codigo_cliente=cli_actual).delete()
    return render(request,"cliente/vercliente.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad,"deletconf":"eliminado"})

def proveedor(request):
    if request.session.get("codigo_usuario"):
        listatabla=Proveedor.objects.all()
        listanacionalidades = Nacionalidad.objects.all()
        listaciudad = Ciudad.objects.all()
        return validar(request,"prov/proveedor.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})
    else:
        return redirect("login")

def modprovee(request, pro_actual = 0):
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            proveedor_actual=Proveedor.objects.filter(codigo_proveedor=pro_actual).exists()
            if proveedor_actual:
                datos_proveedor=Proveedor.objects.filter(codigo_proveedor=pro_actual).first()
                return validar(request, 'prov/modprovee.html',
                {"datos_act":datos_proveedor, "pro_actual":pro_actual, "titulo_f":"Editar un Proveedor", "listanacionalidades":listanacionalidades, "listaciudad":listaciudad} )
            else:
                return validar(request, "prov/modprovee.html", {"titulo_f":"Cargar nuevo Proveedor","pro_actual": pro_actual, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})

        if request.method=="POST":
            if pro_actual==0:
                proveedor_nuevo=Proveedor(codigo_proveedor=request.POST.get('codigo'),
                nombre_proveedor=request.POST.get("nombre"),
                ruc_proveedor=request.POST.get("ruc"),
                telefono_proveedor=request.POST.get("telefono"),
                nacionalidad_id=request.POST.get("nacionalidad") ,
                ciudad_id=request.POST.get("ciudad")
                        
                )
                proveedor_nuevo.save()
            else:
                datos_usuario=Proveedor.objects.filter(codigo_proveedor=pro_actual).first()
                proveedor_nueva=Proveedor2(nombre_proveedor = datos_usuario.nombre_proveedor,
                ruc_proveedor=datos_usuario.ruc_proveedor,
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"),
                telefono_proveedor=datos_usuario.telefono_proveedor,
                nacionalidad=datos_usuario.nacionalidad,
                ciudad=datos_usuario.ciudad,
                codigo_proveedor=datos_usuario.codigo_proveedor)
                proveedor_nueva.save()

                proveedor_actual=Proveedor.objects.get(codigo_proveedor=pro_actual)
                proveedor_actual.nombre_proveedor=request.POST.get("nombre")
                proveedor_actual.ruc_proveedor=request.POST.get("ruc")
                proveedor_actual.telefono_proveedor=request.POST.get("telefono")
                proveedor_actual.nacionalidad_id=request.POST.get("nacionalidad")
                proveedor_actual.ciudad_id=request.POST.get("ciudad")   
                    
                

                proveedor_actual.save()
            
        return redirect("../proveedor")
    else:
        return redirect("login")
    
def borprovee(request, pro_actual):
    listatabla=Proveedor.objects.all()
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    Proveedor.objects.filter(codigo_proveedor=pro_actual).delete()
    return render(request,"prov/proveedor.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad,"deletconf":"eliminado"})

def pais(request):
    if request.session.get("codigo_usuario"):
        listatabla=Nacionalidad.objects.all()
        return validar(request,"direccion/pais.html",{"listatabla":listatabla})
    else:
            return redirect("login")

def modpais(request, pai_actual = 0):
    listanacionalidades = Nacionalidad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            pais_actual=Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).exists()
            if pais_actual:
                datos_pais=Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).first()
                return validar(request, 'direccion/modpais.html',
                {"datos_act":datos_pais, "pai_actual":pai_actual, "titulo_f":"Editar un Pais", "listanacionalidades":listanacionalidades})
            else:
                return validar(request, "direccion/modpais.html", {"titulo_f":"Cargar nuevo Pais","pai_actual": pai_actual, "listanacionalidades":listanacionalidades})

        if request.method=="POST":
            if pai_actual==0:
                pais_nuevo=Nacionalidad(codigo_nacionalidad=request.POST.get('codigo'),
                nacionalidad=request.POST.get("nombre")
                        
                )
                pais_nuevo.save()
            else:
                datos_usuario=Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).first()
                pais_nueva=Nacionalidad2(nacionalidad = datos_usuario.nacionalidad,
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"),
                codigo_nacionalidad=datos_usuario.codigo_nacionalidad)
                      
                pais_nueva.save()
                
                pais_actual=Nacionalidad.objects.get(codigo_nacionalidad=pai_actual)
                pais_actual.nacionalidad=request.POST.get("nombre")            
                
                pais_actual.save()

               
            
        return redirect("../pais")
    else:
        return redirect("login")

def borpais(request, pai_actual):
    listatabla=Nacionalidad.objects.all()
    Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).delete()
    return render(request,"direccion/pais.html",{"listatabla":listatabla,"deletconf":"eliminado"})

def ciudad(request):
    if request.session.get("codigo_usuario"):
        listatabla=Ciudad.objects.all()
        return validar(request,"direccion/ciudad.html",{"listatabla":listatabla})
    else:
        return redirect("login")

def modciudad(request, ciu_actual = 0):
    listaciudades = Ciudad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            ciudad_actual=Ciudad.objects.filter(codigo_ciudad=ciu_actual).exists()
            if ciudad_actual:
                datos_ciudad=Ciudad.objects.filter(codigo_ciudad=ciu_actual).first()
                return validar(request, 'direccion/modciudad.html',
                {"datos_act":datos_ciudad, "ciu_actual":ciu_actual, "titulo_f":"Editar una Ciudad", "listaciudades":listaciudades})
            else:
                return validar(request, "direccion/modciudad.html", {"titulo_f":"Cargar nueva Ciudad","ciu_actual": ciu_actual, "listaciudades":listaciudades})

        if request.method=="POST":
            if ciu_actual==0:
                ciudad_nuevo=Ciudad(codigo_ciudad=request.POST.get('codigo'),
                ciudad=request.POST.get("nombre")
                        
                )
                ciudad_nuevo.save()
            else:
                datos_usuario=Ciudad.objects.filter(codigo_ciudad=ciu_actual).first()
                ciudad_nueva=Ciudad2(ciudad = datos_usuario.ciudad,
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"),
                codigo_ciudad=datos_usuario.codigo_ciudad)
                   
                ciudad_nueva.save()
                
                ciu_actual=Ciudad.objects.get(codigo_ciudad=ciu_actual)
                ciu_actual.ciudad=request.POST.get("nombre")            
                
                ciu_actual.save()

        return redirect("../ciudad")
    else:
        return redirect("login")

def borciudad(request, ciu_actual):
    listatabla=Ciudad.objects.all()
    Ciudad.objects.filter(codigo_ciudad=ciu_actual).delete()
    return validar(request,"direccion/ciudad.html",{"listatabla":listatabla,"deletconf":"eliminado"})

def validar(request, pageSuccess, parameters={}):
    if request.session.get("codigo_usuario"):
        if (request.session.get("tipo_usuario") == 2) and ((pageSuccess == 'user/verusuario.html') or (pageSuccess == 'prov/proveedor.html') or (pageSuccess == 'direccion/pais.html') or (pageSuccess == 'direccion/ciudad.html')):
            return render(request, "index.html", {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "mensaje": "Este usuario no cuenta con los privilegios suficientes"})
        else: 
            return render(request, pageSuccess, {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "parameters": parameters})
    else:
        return render(request, 'login.html')

def vercaja(request):     
    if request.session.get("codigo_usuario"):
        listacaja = Caja.objects.all() 
        return validar(request, "movimiento_caja.html", {"nombre_completo":request.session.get("nombredelusuario"),"listacaja":listacaja})
    else:
        return redirect("login")

def abrir_caja(request, caja_actual=0):
    if request.session.get("codigo_usuario"):
        listacaja = Caja.objects.all()
        if request.method=="GET":
            return validar(request, "abrir_caja.html", {"nombre_completo":request.session.get("nombredelusuario"), "caja_actual":caja_actual,"listacaja":listacaja})
        if request.method=="POST":
            if caja_actual==0:
                    caja_nuevo=Caja(codigo_caja=request.POST.get('codigo_caja'),
                    motivo_caja=request.POST.get('motivo_caja'),
                    fecha_caja=request.POST.get('fecha'),
                    hora_caja=request.POST.get('hora_caja'),
                    entrada_caja=request.POST.get('entrada_caja'),
                    tipo_mov=request.POST.get('tipo_mov'),
                    salida_caja=request.POST.get('salida_caja'),
                    total_caja=request.POST.get('total_caja'),
                    codigo_usuario=request.session.get("codigo_usuario"),
                    nombre_usuario=request.session.get("nombre_completo_usuario"))
                    caja_nuevo.save()
        return redirect("../movimiento_caja")
    else:
        return redirect("login")

def retirar_caja(request, caja_actual=0):
    if request.session.get("codigo_usuario"):
        listacaja=Caja.objects.all()
        if request.method=="GET":
            return validar(request,'retirar_caja.html',{"nombre_completo":request.session.get("nombredelusuario"),"listacaja":listacaja})
        if request.method=="POST":
            if caja_actual==0:
                caja_nuevo=Caja(codigo_caja=request.POST.get('codigo_caja'),
                motivo_caja=request.POST.get('motivo_caja'),
                fecha_caja=request.POST.get('fecha'),
                hora_caja=request.POST.get('hora_caja'),
                entrada_caja=request.POST.get('entrada_caja'),
                tipo_mov=request.POST.get('tipo_mov'),
                salida_caja=request.POST.get('salida_caja'),
                total_caja=request.POST.get('total_caja'),
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"))
                caja_nuevo.save()
        return redirect("../movimiento_caja")
    else:
        return redirect("login")

# def cerrar_caja(request,caja_actual=0):
#     if request.session.get("codigo_usuario"):
#         listacaja=Caja.objects.all()
#         if request.method=="GET":
#             return validar(request,'movimiento_caja.html',{"listacaja":listacaja})
#         if request.method == "POST":
#             if caja_actual==0:
#                 caja_nuevo=Caja(codigo_caja=request.POST.get('codigo_caja'),
#                 motivo_caja=request.POST.get('motivo_caja'),
#                 fecha_caja=request.POST.get('fecha'),
#                 hora_caja=request.POST.get('hora_caja'),
#                 entrada_caja=request.POST.get('entrada_caja'),
#                 tipo_mov=request.POST.get('tipo_mov'),
#                 salida_caja=request.POST.get('salida_caja'),
#                 codigo_usuario=request.session.get("codigo_usuario"),
#                 nombre_usuario=request.session.get("nombre_completo_usuario"),
#                 total_caja=request.POST.get('total_caja'))
#                 caja_nuevo.save()
                
                
#         return redirect("../movimiento_caja")
#     else:
#         return redirect("login")
def cerrar_caja(request,caja_actual=0):
    if request.session.get("codigo_usuario"):
        listacaja=Caja.objects.all()
        if request.method=="GET":
            return validar(request,'movimiento_caja.html',{"listacaja":listacaja})
        if request.method == "POST":
            if caja_actual==0:
                caja_nuevo=Caja(codigo_caja=request.POST.get('codigo_caja'),
                motivo_caja=request.POST.get('motivo_caja'),
                fecha_caja=request.POST.get('fecha'),
                hora_caja=request.POST.get('hora_caja'),
                entrada_caja=request.POST.get('entrada_caja'),
                tipo_mov=request.POST.get('tipo_mov'),
                salida_caja=request.POST.get('salida_caja'),
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"),
                total_caja=request.POST.get('total_caja'))
                caja_nuevo.save()
                
                
        return redirect("../movimiento_caja")
    else:
        return redirect("login")
        
def audirep(request):
    if request.session.get("codigo_usuario"):
        listatabla=producto2.objects.all()
        listacliente=Clientes2.objects.all()
        listaprove=Proveedor.objects.all()
        listaprove2=Proveedor2.objects.all()
        listaciu=Ciudad.objects.all()
        listapai=Nacionalidad.objects.all()
        listaciu2=Ciudad2.objects.all()
        listapai2=Nacionalidad2.objects.all()
        return validar(request,'Auditoria.html',{"listatabla":listatabla,"listacliente":listacliente,"listaprove":listaprove,"listaprove2":listaprove2,"listaciu":listaciu,"listapai":listapai,"listaciu2":listaciu2,"listapai2":listapai2})
    else:
        return redirect("login")     

def venta(request):
    if request.session.get("codigo_usuario"):
        listatabla=producto.objects.all()
        listacliente=Clientes.objects.all()
        return validar(request,'venta.html',{"listatabla":listatabla,"listacliente":listacliente})
    else:
        return redirect("login")

def mod_venta(request,orden_actual=0):
    if request.session.get("codigo_usuario"):
        listaorder=Order.objects.all()
        listatabla=producto.objects.all()
        listacliente=Clientes.objects.all()
        if request.method=="GET":
            return validar(request, "venta.html",{"listaorder":listaorder,"listacliente":listacliente,"listatabla":listatabla})
        if request.method=="POST":
            if orden_actual==0:
                venta_nueva=Order(order_id=request.POST.get('orden_actual'),
                    codigo_producto=request.POST.get('codigo'),
                    precio=request.POST.get('precio'),
                    cantidad=request.POST.get('canti'))
                venta_nueva.save()

        return redirect("../venta/0")     
    else:
        return redirect("login")

class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'venta.html'
    success_url = reverse_lazy('inicio')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = producto.objects.filter(name__icontains=request.POST['term'])[
                        0:10]  # limitante, mostrar de 0 a 10 pdtos
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name  # lo que se va a presentar
                    data.append(item)
                    #Guardado
            elif action == 'add':
                #Metodo de control de Django
                with translation.atomic():#si hay un error no se guarda nada
                    vents = json.loads(request.POST['vents'])#recuperar el valor
                    # inserciones
                    sale = Sale()
                    sale.date_joined = vents['date_joined']
                    sale.cli_id = vents['cli']
                    sale.pay_id = vents['pay']
                    sale.subtotal = float(vents['subtotal'])
                    sale.iva = float(vents['iva'])
                    sale.total = float(vents['total'])
                    sale.save()
                    #iteracion de los productos
                    for i in vents['products']:
                        det = DetSale()
                        det.sale_id = sale.id #relacióon con la factura
                        det.prod_id = i['id'] #relaicón del pdto con su id
                        det.cant = int(i['cant']) #relación con cantidad
                        det.price = float(i['pvp']) #el price de detalle se relaciona con pvp de pdto
                        det.subtotal = float(i['subtotal'])
                        det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  # false para poder serializarse

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Venta'
        context['entity'] = 'Ventas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context



>>>>>>> estilo2venta
