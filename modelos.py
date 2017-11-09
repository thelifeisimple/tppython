class Cliente(object):

    def __init__(self, nombre):
        self.nombre = nombre

		
class Producto(object):

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre


class Venta(Cliente, Producto):

    def __init__(self):
        Cliente.__init__(self)
        Producto.__init__(self)
        self.cantidad = cantidad
        self.precio = precio


Class Ventas(list):

    def __init__(self):
        self.venta = Venta()


class Usuario(object):

    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave


