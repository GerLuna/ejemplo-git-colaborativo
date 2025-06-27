from app.saludo import saludar

def segundoSaludo():
    print("Hola soy el segundo saludo")

if __name__ == "__main__":
    print("Hola soy desconocido")
    nombre = input("¿Cuál es tu nombre? ")
    saludar(nombre)
    segundoSaludo()