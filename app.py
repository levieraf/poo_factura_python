from src.models.Factura import Factura
from src.models.Cliente import Cliente
from src.models.Producto import Producto

def imprimir_factura(factura: Factura):
    print('.............................................................')
    print('Factura Nro: {}'.format(factura.get_numero_factura()))
    print('.............................................................')
    print('Cliente: {}'.format(factura.get_cliente().get_nombre()))

    print('Lista de Productos:')
    for producto in factura.productos():
        print(' - Producto: {}'.format(producto.get_descripcion()))

        if producto.get_descuento() > 0:
            print(' - Precio ({}x{}) = {} con descuento de {}$'.format(producto.get_precio(), producto.get_cantidad(), producto.get_total(), producto.get_descuento()))
        else:
            print(' - Precio ({}x{}) = {}'.format(producto.get_precio(), producto.get_cantidad(), producto.get_total()))

    print('============================================================')
    print('El total a pagar es: {}$'.format(factura.calcular()))
    print('============================================================')

producto_telefono = Producto(descripcion = 'Telefono Samsung', precio = 300, cantidad = 1)
producto_tv = Producto(descripcion = 'Smart TV', precio = 120, cantidad = 1)

cliente = Cliente(nombre = 'Le C.A', email = 'levieraf@gmail.com')
factura = Factura(cliente = cliente)
factura.anadir_producto(Producto(descripcion = 'Telefono Samsung', precio = 300, cantidad = 1, descuento = 10))
imprimir_factura(factura)

cliente = Cliente(nombre = 'Foo Bar', email = 'foobar@gmail.com')
factura = Factura(cliente = cliente)
factura.anadir_producto(producto_telefono)
factura.anadir_producto(Producto(descripcion = 'Telefono Samsung', precio = 300, cantidad = 1))
factura.anadir_producto(producto_telefono)
imprimir_factura(factura)
