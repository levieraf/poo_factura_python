class Producto:
    def __init__(self, **atributos):
        self.__cantidad = atributos['cantidad']
        self.__precio = atributos['precio']
        self.__descripcion = atributos['descripcion']

        if 'descuento' in atributos:
            self.__descuento = atributos['descuento']
        else:
            self.__descuento = 0

    def get_descripcion(self):
        return self.__descripcion

    def get_cantidad(self):
        return self.__cantidad
    
    def get_precio(self):
        return self.__precio

    def get_descuento(self):
        return self.__descuento

    def get_total(self):
        return self.__cantidad * self.__precio

    def get_total_con_descuento(self):
        return self.get_total() - self.__descuento

