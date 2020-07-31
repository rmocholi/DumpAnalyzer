import sys

def extraer_origenes(nombre_archivo):
    """ Procesa un archivo Wireshark en formato csv

    @param nombre_archivo: Nombre del archivo .csv a procesar
    @return Lista ordenada de las ip de origen, sin repeticiones
    """

    # Protocolos que no interesa procesar.
    non_interested = ["ARP", "Protocol"]
    origenes = set()
    with open(nombre_archivo) as file:
        for line in file.readlines():
            try:
                partes = line.split(",")
                source = partes[2][1:-1]
                protocol = partes[4][1:-1]
                if protocol not in non_interested:
                    origenes.add(source)
            except ValueError:
                # Ignoramos cualquier error generado por split
                pass

    lista = list(origenes)
    lista.sort()
    return lista


def extraer_destinos(nombre_archivo):
    """ Procesa un archivo Wireshark en formato csv

    @param nombre_archivo: Nombre del archivo .csv a procesar
    @return Lista ordenada de las ip de destino, sin repeticiones
    """

    # Protocolos que no interesa procesar.
    non_interested = ["ARP", "Protocol"]
    destinos = set()
    with open(nombre_archivo) as file:
        for line in file.readlines():
            try:
                partes = line.split(",")
                destination = partes[3][1:-1]
                protocol = partes[4][1:-1]
                if protocol not in non_interested:
                    destinos.add(destination)
            except ValueError:
                # Ignoramos cualquier error generado por split
                pass

    lista = list(destinos)
    lista.sort()
    return lista



    


