from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # CREACIÓN DE OBJETOS PRODUCTO
    producto1 = Producto("Pizza Margarita", "Comida", "P001", 10, 12.50, True)
    producto2 = Producto("Refresco Cola", "Bebida", "B001", 50, 2.00, True)

    # CREACIÓN DE OBJETOS CLIENTE
    cliente1 = Cliente("Gabriel Mestanza", "@correo.com", 25, True)
    cliente2 = Cliente("Ana Torres", "ana@correo.com", 30, True)

    # Creación de un objeto Restaurante (servicio principal)
    mi_restaurante = Restaurante()

    # Registro de objetos en las listas del restaurante
    mi_restaurante.agregar_producto(producto1)
    mi_restaurante.agregar_producto(producto2)
    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)

    # Visualización de la información
    print("=== PRODUCTOS REGISTRADOS ===")
    mi_restaurante.mostrar_productos()

    print("\n=== CLIENTES REGISTRADOS ===")
    mi_restaurante.mostrar_clientes()

if name == "main":
    main()