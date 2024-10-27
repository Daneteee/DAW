from prettytable import PrettyTable

# Crear una lista de todos los estilos disponibles
estilos_disponibles = [
    "MSWORD_FRIENDLY",
    "PLAIN_COLUMNS",
    "RANDOM",
    "PIPE",
    "ORGANIC",
    "PLAIN",
    "GRID",
    "RST",
    "MARKDOWN",
]

# Crear una tabla
tabla = PrettyTable()

# Definir las columnas
tabla.field_names = ["Estilo", "Tabla"]

# Agregar una fila para cada estilo
for estilo in estilos_disponibles:
    tabla.add_row([estilo, estilo])

# Mostrar la tabla con los estilos
print(tabla)

# Crear una nueva tabla para mostrar las tablas con diferentes estilos
tabla_datos = PrettyTable()

# Definir las columnas
tabla_datos.field_names = ["Estilo", "Tabla"]

# Agregar una fila para cada estilo con una tabla de ejemplo
for estilo in estilos_disponibles:
    tabla_ejemplo = PrettyTable(["Nombre", "Edad", "Ciudad"], **{"style": estilo})
    tabla_ejemplo.add_row(["Juan", 30, "Madrid"])
    tabla_ejemplo.add_row(["María", 25, "Barcelona"])
    tabla_ejemplo.add_row(["Pedro", 35, "Sevilla"])
    tabla_datos.add_row([estilo, tabla_ejemplo])

# Mostrar las tablas con diferentes estilos
print("\nTablas con diferentes estilos:")
print(tabla_datos)
