
paises = input("Ingresar paises seprarados por comas: ")

paises_lista = paises.replace(" ", "").split(",")

paises_lista = set(paises_lista)

paises_lista = sorted(list(paises_lista))

for pais in paises_lista:
    print(f'{pais}, ')


