import random
vet = []
for x in range(50):    
    vet.append(random.randint(0, 100))
print(f'O VETOR QUE FOI CRIADO FOI: {vet}')
for i in range(0, len(vet)):
    
    print(f'valor testado: {vet[i]} | indice testado : {i}')
    
    for j in range(0, len(vet)):
        
        if vet[i] == vet[j] and i != j:
            print(f'INDICE: {j} | VALOR: {vet[j]} \n')