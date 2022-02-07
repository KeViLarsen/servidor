from ssl import ALERT_DESCRIPTION_DECODE_ERROR


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.codigo_productos)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.codigo_productos,
                "nombre": producto.nombre_productos,
                "acumulado": producto.precioventa_productos,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            # if self.carrito [id]["cantidad"] == producto.cantidad_productos:ALERT_DESCRIPTION_DECODE_ERROR("Cantidad maxima del producto alcanzado")
            self.carrito[id]["acumulado"] += producto.precioventa_productos
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.codigo_productos)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.codigo_productos)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precioventa_productos
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True