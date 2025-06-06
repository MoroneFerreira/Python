#%%
'''   
Coleta e amostragem de dados

Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

'''
# %%
#Primeiro Programa
nome = input("Digite seu Nome")
print(f'Olá, {nome}!')
# %%
#Segundo Programa
nome = input("Digite seu Nome")
idade = int(input("Digite sua idade"))
print(f'Olá, {nome}, você tem {idade} anos.')
# %%
#Terceiro Programa
nome = input("Digite seu Nome")
idade = int(input("Digite sua idade"))
altura = float(input('Qual a sua altura?'))
print(f'Olá, {nome}, você tem {idade} anos  mede {altura} metros!')
# %%

'''
Calculadora com operadores
1 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
2 Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
3 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
4 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
5 Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
6 Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
7 Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
8 Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
9 Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
10 Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
'''
#%%
def ajustar_resultado(resultado):
    if resultado.is_integer()==True:
        return(int(resultado))
    else:
        return(resultado)


# %%
#Primeiro Programa
#1 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

valor1 = float(input('Insira o primeiro número para soma'))
valor2 = float(input('Insira o segundo número para soma'))

resultado = valor1+valor2
"Adiciona uma regra que, se o resultado for inteiro, tira o decimal .0, caso não, mantém o decimal"
print(f'O resultado da soma dos valores é igual a {ajustar_resultado(resultado)}')
# %%
#Segundo programa
#2 Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.

valor1 = float(input('Insira o primeiro número para soma'))
valor2 = float(input('Insira o segundo número para soma'))
valor3 = float(input('Insira o terceiro número para soma'))

resultado = valor1+valor2+valor3

print(f'O resultado da soma dos valores é igual a {ajustar_resultado(resultado)}')
# %%
#Terceiro Programa
#3 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

valor1 = float(input('Insira o primeiro número'))
valor2 = float(input('Insira o segundo número'))

resultado = valor1-valor2
print(f'O resultado da subtração é igual a {ajustar_resultado(resultado)}')

# %%
#Quarto Programa
#4 Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.

valor1 = float(input('Insira um numero para multiplicação'))
valor2 = float(input('Insira um segundo número para multiplicação'))

resultado = valor1*valor2

print(f'O resultado da multiplicação é igual a {ajustar_resultado(resultado)}')
# %%
#Quinto Programa
#5 Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

valor1 = float(input('Insira o valor do numerador'))
valor2 = float(input('Insira o valor do denominador - O valor não pode ser igual a 0'))
while valor2==0:
    print('Você inseriu o número 0 como denominador. Tente novamente com um número diferente de zero')
    valor2 = float(input('Insira o valor do denominador - O valor não pode ser igual a 0'))

resultado = valor1/valor2

print(f'O resultado da divisão é {ajustar_resultado(resultado)}')

# %%
#Sexto programa
#6 Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

valor1 = float(input('Insira o valor base da potência'))
valor2 = float(input('Insira o valor do expoente'))

resultado = valor1**valor2

print(f'O resultado da potenciação é igual a {ajustar_resultado(resultado)}')
# %%
#Sétimo programa
#7 Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

valor1 = float(input('Insira o valor do numerador'))
valor2 = float(input('Insira o valor do denominador - O valor não pode ser igual a 0'))
while valor2==0:
    print('Você inseriu o número 0 como denominador. Tente novamente com um número diferente de zero')
    valor2 = float(input('Insira o valor do denominador - O valor não pode ser igual a 0'))

resultado = valor1//valor2

print(f'O resultado inteiro da divisão é {ajustar_resultado(resultado)}')

# %%
#Oitavo programa
#8 Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

valor1 = float(input('Insira o valor do numerador'))
valor2 = float(input('Insira o valor do denominador - O valor não pode ser igual a 0'))
while valor2==0:
    print('Você inseriu o número 0 como denominador. Tente novamente com um número diferente de zero')
    valor2 = float(input('Insira o valor do denominador - O valor não pode ser igual a 0'))

resultado = valor1%valor2

print(f'O resultado do resto da divisão é {ajustar_resultado(resultado)}')
# %%
#Nono programa
#9 Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

nota1 = float(input('Insira a primeira nota'))
nota2 = float(input('Insira a segunda nota'))
nota3 = float(input('Insira a terceira nota'))

resultado = (nota1+nota2+nota3)/3

print(f'A média é igual a {ajustar_resultado(resultado)}')
# %%
#Décimo programa
#10 Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

valores = [5,12,20,15]
pesos = [1,2,3,4]

media_ponderada = ((valores[0]*pesos[0])+(valores[1]*pesos[1])+(valores[2]*pesos[2])+(valores[3]*pesos[3])/sum(pesos))
print(f'A média ponderada dos valores é igual a {ajustar_resultado(media_ponderada)}')

# %%
#Exercícios de texto
##Editando textos
'''
1 Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
2 Crie um código que solicite uma frase e depois imprima a frase na tela.
3 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
4 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
5 Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
6 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
7 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
8 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
9 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
10 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
'''
# %%
#Exercício 1
#1 Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.

frase = "Olá, Mundo!"
print(frase)
# %%
#Exercício 2
#2 Crie um código que solicite uma frase e depois imprima a frase na tela.

frase = input("Escreva uma frase")
print(frase)
# %%
#Exercício 3
#3 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.

frase = input("Escreva uma frase")
print(str.upper(frase))
# %%
#Exercício 4
#4 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.

frase = input("Escreva uma frase")
print(str.lower(frase))
# %%
#Exercício 5
#5 Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

frase = "   Olá! Estou aprendendo Python para Ciência de Dados "
print(str.strip(frase))
# %%
#Exercício 6
#6 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.

frase = input("Escreva uma frase")
print(str(frase).strip())
# %%
#Exercício 7
#7 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input("Escreva uma frase")
print(str(frase).strip().lower())

# %%
#Exercício 8
#8 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.

frase = input("Escreva uma frase")
print(str(frase).replace('e','f').replace('E','f'))

#%%
#Exercício 9
#9 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input("Escreva uma frase")
print(str(frase).replace('a','@').replace('à','@').replace('á','@').replace('â','@').replace('ã','@'))

#%%
#Exercício 10
#10 Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input("Escreva uma frase")
print(str(frase).replace('s','$').replace('S','$'))
# %%
