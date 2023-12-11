#Manipulação de Strings:

#Escreva uma função para verificar se uma string é um palíndromo.
#Implemente uma função que conte o número de vogais em uma string.

palavra = ['tenet']

string_invertida = ''.join(reversed(palavra[0]))
if palavra[0] == string_invertida:

    print('correto')
else:
      print('Errado')


palavra = 'o maior mundo'
palavra2 = []
vogais = ['a', 'e', 'i', 'o', 'u']

for i in palavra:
    if i in vogais:
        palavra2.append(i)

print(palavra2, 'numeros de vogais =',len(palavra2))
