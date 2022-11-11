class Factura:
    contador_factura = 0

    def __init__(self, **atributos):
        self.__cliente = atributos['cliente']
        self.__productos = []
        Factura.contador_factura = Factura.contador_factura + 1
    
    def anadir_producto(self, producto):
        self.__productos.append(producto)

    def get_numero_factura(self):
        return Factura.contador_factura

    def get_cliente(self):
        return self.__cliente
    
    def productos(self):
        return self.__productos

    def calcular(self):
        sum_total = 0
        for producto in self.__productos:
            sum_total = sum_total + producto.get_total_con_descuento()

        return sum_total
