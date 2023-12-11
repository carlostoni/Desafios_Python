#Manipulação de Listas:

#Crie uma lista com números inteiros e remova os elementos duplicados.
#Crie uma lista de strings e ordene-a em ordem alfabética reversa.

numeros = [1, 2, 3, 4, 4, 5, 6, 7, 8, 7, 9, 10]

print(list(set(numeros)))

palavras = ['amor', 'verdade', 'sushi']

n= sorted(palavras, reverse=True)

print(n)
