class Producto:
    def _init_(self, nombre: str, categoria: str, codigo: str, cantidad: int, precio: float, disponible: bool):
        # Identificadores descriptivos para almacenar información del producto
        self.nombre = nombre
        self.categoria = categoria
        self.codigo = codigo
        # Tipos de datos numéricos
        self.cantidad = cantidad
        self.precio = precio
        # Tipo de dato lógico
        self.disponible = disponible

    def mostrar_informacion(self) -> str:
        # Retorna info principal del producto
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Stock: {self.cantidad}"

    def _str_(self) -> str:
        # Representación en texto del objeto Producto
        return f"{self.nombre} | {self.categoria} | ${self.precio}"
