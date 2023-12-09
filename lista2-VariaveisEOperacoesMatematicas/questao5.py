"""
Q5. Escreva um algoritmo que solicita ao usuário uma quantidade de tempo em metros e 
então a converte para centimetros. Por exemplo, se o usuário inserir 2 metros,
o programa deve imprimir "200 centímetros".
"""

valorConverter = int(input("qual valor será convertido para centimetros?"));

valorConvertido = valorConverter * 100;

print(f"em centimetros {valorConverter}m equivale á {valorConvertido}cm");