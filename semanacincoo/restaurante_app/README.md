# Proyecto: Sistema de Gestión de Restaurante

*Estudiante:* Mariela Stefanía García Villacís

## Descripción del Sistema
Este sistema fue desarrollado como una aplicación básica de gestión para un restaurante, permitiendo la administración eficiente de los platos ofrecidos en el menú y los comensales registrados en el establecimiento. El proyecto utiliza Programación Orientada a Objetos (POO) para separar las entidades (modelos) de la lógica de negocio (servicios).

## Estructura del Proyecto
El proyecto está organizado de forma modular para garantizar la escalabilidad y el orden:
* restaurante_app/
    * modelos/: Contiene las clases Plato y Comensal, que definen las estructuras de datos básicas.
    * servicios/: Contiene la clase GestionRestaurante, encargada de administrar las colecciones de objetos y las operaciones principales.
    * main.py: Punto de entrada del programa donde se instancian los objetos y se ejecuta la lógica.

## Tipos de Datos Utilizados
Para asegurar la integridad de la información, se han definido los siguientes tipos de datos en las clases:
* *Strings (str):* Utilizados para nombres de platos y nombres de clientes.
* *Floats (float):* Utilizados para representar los precios de los productos.
* *Enteros (int):* Utilizados para el número de mesa.
* *Booleanos (bool):* Utilizados para indicadores lógicos, como si un plato es picante.
* *Listas (list):* Utilizadas dentro de la clase de servicios para almacenar y gestionar múltiples instancias de objetos.

## Reflexión sobre la Programación Modular
La implementación de este sistema demuestra que el uso de *identificadores descriptivos* es fundamental para que el código sea legible y mantenible por otros desarrolladores. La elección de *tipos de datos adecuados* garantiza que la información se manipule correctamente desde el inicio, evitando errores de ejecución. Finalmente, el uso de *listas* dentro de una arquitectura modular es vital, ya que permite separar la responsabilidad de almacenamiento de la lógica operativa, facilitando que el software sea robusto, organizado y fácil de escalar a medida que el restaurante crece