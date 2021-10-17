#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Calculadora em python

# Definir as operações da calculadora e o que elas retornarão

def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y

def pot (x,y):
    return x ** y

# Print das opções que o usuário terá direito a escolher

print ('\nSelecione o número da operação')
print ('1 - soma')
print ('2 - subtração')
print ('1 - multiplicação')
print ('1 - divisão')
print ('1 - potência')

# Variável para armazenar a opção escolhida

escolha = input('\nDigite sua opção (1/2/3/4/5): ')

# Variáveis para armazenar os dois números que o usuário escolherá

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))

# Estrutura If para calcular os valores escolhidos pelo usuário de acordo com a opção escolhida para a operação

if escolha == "1":
    print("\n")
    print(num1, "+", num2,"=", add(num1,num2))
    print('\n')
    
elif escolha == '2':
    print('\n')
    print(num1, "-", num2, '=', subtract(num1,num2))
    print('\n')

elif escolha == '3':
    print('\n')
    print(num1, "*", num2, '=', multiply(num1,num2))
    print('\n')
    
elif escolha == '4':
    print('\n')
    print(num1, "/", num2, '=', divide(num1,num2))
    print('\n')
    
elif escolha == '5':
    print('\n')
    print(num1, "^", num2, '=', pot(num1,num2))
    print('\n')
    
# Caso o usuário escolha uma opção diferente de 1 a 5 será retornado a mensagem "Opção Inválida!"    
    
else:
    print('\nOpção inválida!')


# In[ ]:




