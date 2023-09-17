Estudiantes = [
    "Juan,98,87,89,90",
    "Jose,90,43,20,40",
    "Pedro,70,80,89,90"
]

# Función para calcular el promedio de las notas de un estudiante
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Procesar la lista de Estudiantes y calcular los promedios
promedios = {}
for Estudiante in Estudiantes:
    datos = Estudiante.split(',')
    nombre = datos[0]
    notas = list(map(int, datos[1:]))
    promedio = calcular_promedio(notas)
    promedios[nombre] = promedio

# Guardar los resultados en un archivo de texto
with open("promedios.txt", "w") as archivo:
    for nombre, promedio in promedios.items():
        archivo.write(f"{nombre}={promedio:.2f}\n")

print("Los promedios se han guardado en el archivo 'promedios.txt'")