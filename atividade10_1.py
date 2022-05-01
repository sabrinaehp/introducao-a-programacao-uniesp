'''Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.'''

tamanho = 20
lista = []

for indice in range(tamanho):
    numero = int(input('Digite um número: '))
    lista.append(numero)

for indice in reversed(lista):
    print(indice)
