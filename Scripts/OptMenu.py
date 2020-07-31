import sys
from .SwitcherClass import Switcher
#Funciones

def imprimir():
    print("________________________")
    print()
    print("Bienvenido al Analizador de Tramas de la UTM")
    print("________________________")
    print()
    print("Opciones disponibles:")
    print("1. Peticiones aglomeradas")
    print("2. Extraer IP's Origen totales")
    print("3. Extraer IP's Destino totales")
    print("0. Salir")
    print()


def menu():
    doc = ""

    while True:
        imprimir()
        #Si el documento a analizar no esta inicializado entramos en este bloque para inicializarlo
        if doc == "":
            try:
                doc = input("Escriba la ruta del documento a analizar(Si el documento está en la misma carpeta, introduzca solo el nombre del archivo): ")
                sweety=Switcher(doc)
                
            except FileNotFoundError:
                print("Error, Escriba una dirección válida")
                break
           
        else:
            pass
        
        try:
            entrada_usuario = int(input("Seleccione una opcion: "))

            if entrada_usuario in range(4):

                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    break
                print()
                sweety.opcionificacionacion(entrada_usuario)
            else:
                print('Error, solo de aceptan numeros del 0 al 3')

        except ValueError:
            print("Error, ingrese solamente numeros")


#Ejecución
