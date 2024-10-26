import sys

class Estudiante:
    numero_estudiante = ""
    nombre_completo = ""
    apellido_completo = ""

    def __init__(self, num_est, nombre, apellido):
        self.numero_estudiante = num_est
        self.nombre_completo = nombre
        self.apellido_completo = apellido

    def __str__(self):
        return f"Número de Estudiante: {self.numero_estudiante}, Nombres: {self.nombre_completo}, Apellidos: {self.apellido_completo}"

class PilaEstudiantes:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return not self.elementos

    def agregar(self, estudiante):
        self.elementos.append(estudiante)

    def remover(self):
        if self.esta_vacia():
            return "No hay estudiantes en la pila para remover."
        return self.elementos.pop()

    def ver_tope(self):
        if self.esta_vacia():
            return "La pila está vacía."
        return self.elementos[-1]

    def contar(self):
        return len(self.elementos)

    def mostrar_todos(self):
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            for est in reversed(self.elementos):
                print(est)

class ColaEstudiantes:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return not self.elementos

    def agregar(self, estudiante):
        self.elementos.insert(0, estudiante)

    def remover(self):
        if self.esta_vacia():
            return "No hay estudiantes en la cola para remover."
        return self.elementos.pop()

    def contar(self):
        return len(self.elementos)

    def mostrar_todos(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            for est in self.elementos:
                print(est)

def iniciar_menu():
    pila_estudiantes = PilaEstudiantes() 
    cola_estudiantes = ColaEstudiantes()

    opciones = {
        "1": ("Agregar estudiante a la pila", pila_estudiantes.agregar),
        "2": ("Remover estudiante de la pila", pila_estudiantes.remover),
        "3": ("Mostrar todos los estudiantes en la pila", pila_estudiantes.mostrar_todos),
        "4": ("Agregar estudiante a la cola", cola_estudiantes.agregar),
        "5": ("Remover estudiante de la cola", cola_estudiantes.remover),
        "6": ("Mostrar todos los estudiantes en la cola", cola_estudiantes.mostrar_todos),
        "7": ("Salir", None)
    }

    while True:
        print("\n=== Gestión de Estudiantes (Pilas y Colas) ===")
        for key, (description, _) in opciones.items():
            print(f"{key}. {description}")

        opcion = input("Elija una opción: ")

        if opcion in opciones:
            if opcion == "7":
                print("Cerrando el programa...")
                break
            elif opcion in ["1", "4"]:
                num_est = input("Número de estudiante: ")
                nombre = input("Nombre del estudiante: ")
                apellido = input("Apellido del estudiante: ")
                estudiante = Estudiante(num_est, nombre, apellido)
                opciones[opcion][1](estudiante)
                print(f"Estudiante añadido exitosamente a la {'pila' if opcion == '1' else 'cola'}.\n")
            else:
                resultado = opciones[opcion][1]()
                if resultado:
                    print(resultado)
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    sys.exit(iniciar_menu())
