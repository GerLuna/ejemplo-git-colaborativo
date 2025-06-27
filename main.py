from app.saludo import saludar

if __name__ == "__main__":
    print("Hola desconocido")
    nombre = input("¿Cuál es tu nombre? ")
    saludar(nombre)
