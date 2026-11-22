"""Doc string"""
import math

NOME = "Heitor"


print(NOME)
print(NOME)
print(NOME)
print(NOME)

print(math.acos(1))

def dividir(a: int, b: int) -> float:
    """Funcao dividir\n
    Recebe dois e divide o 1ª pelo º"""

    print(a, b)
    return a / b

def processar_lista(numeros):
    """Processa uma lista de numeros"""
    total = 0
    for n in numeros:
        total += dividir(10, n)
    return total

lista = [2, 5, 0, 4]  # O zero aqui vai causar problema!
resultado = processar_lista(lista)
print("Resultado:", resultado)
