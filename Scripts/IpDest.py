import sys

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
                source = partes[2][1:-1]
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: extrae.py nombre_archivo")
    else:
        lista = extraer_destinos(sys.argv[1])
        for dest in lista:
            print(dest)