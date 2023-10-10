quant = int(input("Digite a quantidade de numeros que você quer na lista: "))
numeros = []

for x in range(quant):
    num = int(input("Digite o numero: "))
    
    numbers = {
        'Numero': num,
    }
    
    numeros.append(numbers)

with open('numeros_inteiros.txt', 'w') as arquivo:
    for numero in numeros:
        arquivo.write(f"Numero: {numero['Numero']}\n")
