estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}
def agregar ():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad: "))
    materias = []
    materia = input("Ingrese una materia aprobada (o presione Enter para finalizar): ")
    while materia:
        materias += [materia]  # Se usa concatenación en lugar de append
        materia = input("Ingrese otra materia aprobada (o presione Enter para finalizar): ")
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print(f"Estudiante {nombre} agregado correctamente.")

def mostrar():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for nombre, datos in estudiantes.items():
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {datos['materias']}")

def eliminar():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print("Estudiante no encontrado.")
def buscar():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {datos['materias']}")
    else:
        print("Estudiante no encontrado.")
def clave():
    palabra = input("Ingrese una palabra clave para buscar en los nombres: ")
    encontrados = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower()]
    if encontrados:
        print("Coincidencias encontradas:")
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print("No se encontraron coincidencias.")
op = 0
while op != 6:
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Buscar estudiante")
    print("5. Verificar palabra clave en nombres")
    print("6. Salir")
    op = int(input("Seleccione una opción: "))  # Cambié la entrada para que sea un número entero
    match op:
        case 1:
            agregar()
        case 2:
            mostrar()
        case 3:
            eliminar()
        case 4:
            buscar()
        case 5:
            clave()
        case 6:
            print("Saliendo del programa...")
        case _:
            print("Opción no válida. Intente de nuevo.")


