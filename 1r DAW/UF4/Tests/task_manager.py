class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = nueva_edad


# Ejemplo de uso
persona = Persona("Juan", 30)
print(persona.nombre)  # Salida: Juan
print(persona.edad)    # Salida: 30

persona.nombre = "Pedro"
persona.edad = 25

print(persona.nombre)  # Salida: Pedro
print(persona.edad)    # Salida: 25
