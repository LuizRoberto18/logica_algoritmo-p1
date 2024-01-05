"""
Q4. Faça um algoritmo que lê dois números, e verifica se o primeiro número é igual ao segundo número. 
Se forem iguais, escrever "Números iguais". 
Se não, escrever "Números diferentes".
"""
n1 = int(input("digite o primeiro numero:\n"));
n2 =int(input("digite o segundo numero:\n"));

if(n1 == n2):
    print("o numero {} é igual ao numero {}".format(n1,n2));
else:
    print("o numero {} não é igual ao numero {}".format(n1,n2));