"""
Q3.  Faça um programa que leia o nome de uma pessoa e a sua idade. 
Imprima uma mensagem que diga "Olá, [nome]. Você terá  [idade] anos daqui a 10 anos".
Os dados de entrada devem ser armazenados em variáveis distintas. Para o processamento, considere o ano atual.
"""

nome = input("Me diga seu nome: ");
print("Ok");
idade = int(input("Agora me diga sua idade: "));  # Converte a entrada para inteiro
novaIdade = idade + 10;  # Adiciona 10 à idade
print(f"{nome}, você tem {idade} anos e daqui a 10 anos você terá {novaIdade} anos.");