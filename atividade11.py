import random

m = []

for x in range(1,11):
    
    lista_auxiliar = []

    for y in range(1,11):
        lista_auxiliar.append(random.randint(1, 1000))

    print("Adicionando na Matriz")  
    print(lista_auxiliar)
    m.append(lista_auxiliar)

print("Nossa Matriz")    
print(m)