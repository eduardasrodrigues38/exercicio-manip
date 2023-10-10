def calcular_media(numeros):
    if not numeros:
        return 0
    total = sum(numeros)
    return total / len(numeros)

numeros = []

with open('numeros_inteiros.txt', 'r') as arquivo:
    for linha in arquivo:
        numero = int(linha.split(': ')[1].strip())
        numeros.append(numero)

media = calcular_media(numeros)

print(f'A media e: {media}.')
