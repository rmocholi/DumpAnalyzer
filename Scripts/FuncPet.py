import sys
from .peticionesClass import peticion

def petAglom(archivo):
    lista = set()
    non_interested = ["ARP", "Protocol"]

    with open(archivo) as file:
        for line in file.readlines():
            try:
                partes = line.split(",")
                source = partes[2][1:-1]
                destination = partes[3][1:-1]
                protocol = partes[4][1:-1]
                info = partes[6][1:-1]
                if protocol not in non_interested:
                    p = peticion(source,destination,protocol)
                    if p in lista:
                        pass
                    else:
                        with open(archivo) as file:
                            for line in file.readlines():
                                try:
                                    prts = line.split(",")
                                    src = prts[2][1:-1]
                                    dst = prts[3][1:-1]
                                    prtcl = prts[4][1:-1]
                                    inf = prts[6][1:-1]

                                    if prtcl not in non_interested:
                                        c=peticion(src,dst,prtcl)
                                        if c == p:
                                            p.NoTimes += 1

                                except ValueError:
                                    # Ignoramos cualquier error generado por split
                                    pass
                        lista.add(p)

            except ValueError:
                # Ignoramos cualquier error generado por split
                pass
    
    return lista


def printPetAglom(archivo):
    lista = petAglom(archivo)
    print('"Origen","Destino","Protocolo","Nº"')
    for pet in lista:
        print(pet)

def savePetAglom(archivo):
    lista = petAglom(archivo)
    with open("PeticionesAglomeradas.csv","w") as f:
        f.write('"Origen","Destino","Protocolo","Nº"'+ '\n')
        for pet in lista:
            f.write(print(pet)+'\n')
        
    print('Hecho.')

