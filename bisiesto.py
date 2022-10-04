def anioBisiesto(anio):
    if (anio % 4 == 0) and ((anio % 400 == 0) or not(anio % 100 == 0)):
        print(anio, " es año bisiesto.")
    else:
        print(anio, " no es año bisiesto.")

anio = (int)(input("Ingrese el año: "))
anioBisiesto(anio)
