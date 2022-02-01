from collections import namedtuple
from django.shortcuts import render, redirect
from django.db.models import Q
from vapunto.models import *
from vapunto.models import producto


def login(request):
    if request.method == "GET":
        if request.session.get("nombre_usuario"):
            return redirect("index.html")
        else: 
            return render(request, 'inicio')
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
                return render(request, 'loging.html', {"mensaje_error":"Contraseña ingresada es incorrecta."})
        else:
            return render(request, 'loging.html', {"mensaje_error":"Usuario ingresado no existe."})

def inicio(request):

    if request.session.get("nombredelusuario"):
        return render(request, 'index.html', {"nombre_usuario": request.session.get("nombre_completo_usuario")})
    else:
        return render(request, 'login.html')

def salir(request):
    request.session.flush()
    return redirect('login.html')
    
def tabla(request):
    return render(request,'tables.html')

def venta(request):
    listatabla=producto.objects.all()
    return render(request,'venta.html',{"listatabla":listatabla})
    
def product(request):
    if request.session.get("codigo_usuario"):
        listatabla=producto.objects.all()
        return render(request,"produ/product.html",{"listatabla":listatabla})
    else:
         return redirect("login.html")

def modproducto(request, prod_actual = 0):
    if request.session.get("codigo_usuario"):
            if request.method=="GET":
                producto_actual=producto.objects.filter(codigo_productos=prod_actual).exists()
                if producto_actual:
                    datos_producto=producto.objects.filter(codigo_productos=prod_actual).first()
                    return render(request, 'produ/modproducto.html',
                    {"datos_act":datos_producto, "prod_actual":prod_actual, "titulo_f":"Editar un Producto"})
                else:
                    return render(request, "produ/modproducto.html", {"titulo_f":"Cargar nuevo Producto","prod_actual": prod_actual})

            if request.method=="POST":
                if prod_actual==0:
                    producto_nuevo=producto(codigo_productos=request.POST.get('codigo'),
                    nombre_productos=request.POST.get("nombre"),
                    preciocompra_productos=request.POST.get("costo"),
                    precioventa_productos=request.POST.get("venta"),
                    categoria_productos=request.POST.get("categoria"),
                    cantidad_productos=request.POST.get("cantidad"),
                            
                    )
                    producto_nuevo.save()
                else:
                    producto_actual=producto.objects.get(codigo_productos=prod_actual)
                    producto_actual.nombre_productos=request.POST.get("nombre")
                    producto_actual.preciocompra_productos=request.POST.get("costo")
                    producto_actual.precioventa_productos=request.POST.get("venta")
                    producto_actual.categoria_productos=request.POST.get("categoria")
                    producto_actual.cantidad_productos=request.POST.get("cantidad")
                    producto_actual.save()
                
            return redirect("../product")
    else:
         return redirect("login.html")
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
                return render(request, "user/modusuario.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_s":"Modificar Usuario", 
                "subtitulo_s":"Vuleva a escribir los datos que desea modificar", 
                "datos_act":datos_usuario, 
                "usu_actual":usu_actual})
            else:
                return render(request, "user/modusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
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
        return render(request, "user/verusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"),
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
        return render(request,"cliente/vercliente.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})
    else:
         return redirect("login.html")
    
def modcliente(request, cli_actual = 0):
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            cliente_actual=Clientes.objects.filter(codigo_cliente=cli_actual).exists()
            if cliente_actual:
                datos_cliente=Clientes.objects.filter(codigo_cliente=cli_actual).first()
                return render(request, 'cliente/modcliente.html',
                {"datos_act":datos_cliente, "cli_actual":cli_actual, "titulo_f":"Editar un Cliente", "listanacionalidades":listanacionalidades, "listaciudad":listaciudad} )
            else:
                return render(request, "cliente/modcliente.html", {"titulo_f":"Cargar nuevo Cliente","cli_actual": cli_actual, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})

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
                cliente_actual=Clientes.objects.get(codigo_cliente=cli_actual)
                cliente_actual.nombre_cliente=request.POST.get("nombre")
                cliente_actual.apellido_cliente=request.POST.get("apellido")
                cliente_actual.ruc_cliente=request.POST.get("ruc")
                cliente_actual.telefono_cliente=request.POST.get("telefono")
                cliente_actual.nacionalidad_id=request.POST.get("nacionalidad")
                cliente_actual.ciudad_id=request.POST.get("ciudad")
                
                datos_usuario=Clientes.objects.filter(codigo_cliente=cli_actual).first()
                cliente_nueva=Clientes2(nombre_cliente = datos_usuario.nombre_cliente,
                ruc_cliente=datos_usuario.ruc_cliente,
                codigo_usuario=request.session.get("codigo_usuario"),
                nombre_usuario=request.session.get("nombre_completo_usuario"),
                apellido_cliente=datos_usuario.apellido_cliente,
                telefono_cliente=datos_usuario.telefono_cliente,
                nacionalidad=datos_usuario.nacionalidad,
                ciudad=datos_usuario.ciudad)

                cliente_nueva.save()

            
            
                cliente_actual.save()

        return redirect("../vercliente")
    else:
        return redirect("login.html")
        
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
        return render(request,"prov/proveedor.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})
    else:
        return redirect("login.html")

def modprovee(request, pro_actual = 0):
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            proveedor_actual=Proveedor.objects.filter(codigo_proveedor=pro_actual).exists()
            if proveedor_actual:
                datos_proveedor=Proveedor.objects.filter(codigo_proveedor=pro_actual).first()
                return render(request, 'prov/modprovee.html',
                {"datos_act":datos_proveedor, "pro_actual":pro_actual, "titulo_f":"Editar un Proveedor", "listanacionalidades":listanacionalidades, "listaciudad":listaciudad} )
            else:
                return render(request, "prov/modprovee.html", {"titulo_f":"Cargar nuevo Proveedor","pro_actual": pro_actual, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad})

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
                proveedor_actual=Proveedor.objects.get(codigo_proveedor=pro_actual)
                proveedor_actual.nombre_proveedor=request.POST.get("nombre")
                proveedor_actual.ruc_proveedor=request.POST.get("ruc")
                proveedor_actual.telefono_proveedor=request.POST.get("telefono")
                proveedor_actual.nacionalidad_id=request.POST.get("nacionalidad")
                proveedor_actual.ciudad_id=request.POST.get("ciudad")
                
                
                proveedor_actual.save()
            
        return redirect("../proveedor")
    else:
        return redirect("login.html")
    
def borprovee(request, pro_actual):
    listatabla=Proveedor.objects.all()
    listanacionalidades = Nacionalidad.objects.all()
    listaciudad = Ciudad.objects.all()
    Proveedor.objects.filter(codigo_proveedor=pro_actual).delete()
    return render(request,"prov/proveedor.html",{"listatabla":listatabla, "listanacionalidades":listanacionalidades, "listaciudad":listaciudad,"deletconf":"eliminado"})

def pais(request):
    if request.session.get("codigo_usuario"):
        listatabla=Nacionalidad.objects.all()
        return render(request,"direccion/pais.html",{"listatabla":listatabla})
    else:
            return redirect("login.html")
def modpais(request, pai_actual = 0):
    listanacionalidades = Nacionalidad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            pais_actual=Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).exists()
            if pais_actual:
                datos_pais=Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).first()
                return render(request, 'direccion/modpais.html',
                {"datos_act":datos_pais, "pai_actual":pai_actual, "titulo_f":"Editar un Pais", "listanacionalidades":listanacionalidades})
            else:
                return render(request, "direccion/modpais.html", {"titulo_f":"Cargar nuevo Pais","pai_actual": pai_actual, "listanacionalidades":listanacionalidades})

        if request.method=="POST":
            if pai_actual==0:
                pais_nuevo=Nacionalidad(codigo_nacionalidad=request.POST.get('codigo'),
                nacionalidad=request.POST.get("nombre")
                        
                )
                pais_nuevo.save()
            else:
                pai_actual=Nacionalidad.objects.get(codigo_nacionalidad=pai_actual)
                pai_actual.nacionalidad=request.POST.get("nombre")            
                
                pai_actual.save()
            
        return redirect("../pais")
    else:
        return redirect("login.html")

def borpais(request, pai_actual):
    listatabla=Nacionalidad.objects.all()
    Nacionalidad.objects.filter(codigo_nacionalidad=pai_actual).delete()
    return render(request,"direccion/pais.html",{"listatabla":listatabla,"deletconf":"eliminado"})

def ciudad(request):
    if request.session.get("codigo_usuario"):
        listatabla=Ciudad.objects.all()
        return render(request,"direccion/ciudad.html",{"listatabla":listatabla})
    else:
        return redirect("login.html")
def modciudad(request, ciu_actual = 0):
    listaciudades = Ciudad.objects.all()
    if request.session.get("codigo_usuario"):
        if request.method=="GET":
            ciudad_actual=Ciudad.objects.filter(codigo_ciudad=ciu_actual).exists()
            if ciudad_actual:
                datos_ciudad=Ciudad.objects.filter(codigo_ciudad=ciu_actual).first()
                return render(request, 'direccion/modciudad.html',
                {"datos_act":datos_ciudad, "ciu_actual":ciu_actual, "titulo_f":"Editar una Ciudad", "listaciudades":listaciudades})
            else:
                return render(request, "direccion/modciudad.html", {"titulo_f":"Cargar nueva Ciudad","ciu_actual": ciu_actual, "listaciudades":listaciudades})

        if request.method=="POST":
            if ciu_actual==0:
                pais_nuevo=Ciudad(codigo_ciudad=request.POST.get('codigo'),
                ciudad=request.POST.get("nombre")
                        
                )
                pais_nuevo.save()
            else:
                ciu_actual=Ciudad.objects.get(codigo_ciudad=ciu_actual)
                ciu_actual.Ciudad=request.POST.get("nombre")            
                
                ciu_actual.save()
            
        return redirect("../ciudad")
    else:
        return redirect("login.html")

def borciudad(request, ciu_actual):
    listatabla=Ciudad.objects.all()
    Ciudad.objects.filter(codigo_ciudad=ciu_actual).delete()
    return render(request,"direccion/ciudad.html",{"listatabla":listatabla,"deletconf":"eliminado"})


# Create your views here.
