
from functools import reduce

elementos = [1,2,3,4,5,6,7,8,9]

filtro = filter(lambda x: x % 2 == 1, elementos)

suma_impares = reduce(lambda a,b: a+b, filtro)

print(suma_impares)
