'''
Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.
'''

VET = [1, 2, 3, 1]
repetidos = []
tamanho = 4


 for i in range(tamanho):
     numero = int(input('Digite um número: '))
     VET.append(numero)


 for i in range(1, 4):
   for j in range(i+1, 4):
     if VET[i] == VET[j]:
       print(f'O numero {VET[i]} foi repetido na posição {i}')

 for i in range(tamanho):

     if VET[i] == VET[i+1]:
         print(f'O valor {VET[i]} foi repetido na posição {i}')
