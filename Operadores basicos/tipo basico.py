inteiro = 10 # int(Numero inteiro)
decimal = 3.14159 # Float (Numero decimal)
complexo = 3+4j # complex (Numero complexo)

print (inteiro, decimal, complexo)
print (f"Tipos: {type(inteiro)}, {type(decimal)}, {type(complexo)}")

# Texto
Texto = "Ola mundo!" #str (string / texto)
print(f"Tipos: {type(Texto)}")

# Booleanos
verdadeiro = True # bool (booleano verdadeiro)
falso = False # bool (booleano falso)
print (verdadeiro, falso)
print(f"Tipos: {type(verdadeiro)}, {type(falso)}")

#colecoes
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list (lista mutavel)
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # tupla (tupla imutavel)
dicionario = {"Nome": "Sebastiao"} # dic (dicionario)
conjunto = {1, 2, 3, 4} # ser(conjunto)
print (lista, tupla, dicionario, conjunto)
print(f"Tipos: {type(lista)}, {type(tupla)}, {type(dicionario)}, {type(conjunto)}")

# o comando input () e utilizado em python
nome = input("Digite seu nome: ")
print(f"Ola , {nome}! Bem-vindo ao Python! ")
idade = int(input("Digite sua idade: "))
print(f"Daqui a 5 anos, voce tera {idade+5} anos!")