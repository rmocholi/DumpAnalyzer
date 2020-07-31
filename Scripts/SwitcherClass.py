from . import FuncIP
from . import FuncPet

class Switcher():
    doc = ""

    def __init__(self,docu):
        self.doc = docu

    def opcionificacionacion(self, argument):
        """Dispatch method"""
        method_name = 'opt_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid option")
        # Call the method as we return it
        return method()
 
 #Peticiones aglomeradas
    def opt_1(self):
        FuncPet.printPetAglom(self.doc)
        deseo = input("Desea guardar los resultados en un archivo de texto?(s/n) ")
        if deseo == 's':
            FuncPet.savePetAglom(self.doc)
        else:
            pass

 
 #IP's Origen
    def opt_2(self):
       print(FuncIP.extraer_origenes(self.doc)) 
 
 #IP's Destino
    def opt_3(self):
        print(FuncIP.extraer_destinos(self.doc))