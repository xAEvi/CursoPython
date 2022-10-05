def main():
    fichero = "hola.txt"

    datos = [
        'adios',
        'adios, saludos'
    ]

    lectura = leerFichero(fichero)
    mostrarLectura(lectura)

    escribirFichero(fichero, datos)

    lectura = leerFichero(fichero)
    mostrarLectura(lectura)


def leerFichero(fichero):
    f = open(fichero, 'r')
    lineas = f.readlines()
    f.close()
    return lineas


def escribirFichero(fichero, datos):
    f = open(fichero, 'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea += '\n'

        f.write(linea)
    f.close()


def mostrarLectura(lectura):
    for linea in lectura:
        print(linea)


if __name__ == '__main__':
    main()
