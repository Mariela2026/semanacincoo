class Cliente:
    def _init_(self, nombre: str, correo: str, edad: int, activo: bool):
        # Identificadores descriptivos para almacenar información del cliente
        self.nombre = nombre
        self.correo = correo
        # Tipo de dato numérico entero
        self.edad = edad
        # Tipo de dato lógico
        self.activo = activo

    def mostrar_informacion(self) -> str:
        # Retorna info principal del cliente
        return f"{self.nombre} | {self.correo}"

    def _str_(self) -> str:
        # Representación en texto del objeto Cliente
        return f"{self.nombre} ({self.edad} años)"
