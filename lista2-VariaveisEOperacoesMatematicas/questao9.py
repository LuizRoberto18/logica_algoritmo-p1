"""
Q9. Área de um Triângulo: Escreva um algoritmo que solicita ao usuário a base e a altura de um triângulo, 
depois calcula e exibe a área do triângulo. 
A fórmula para calcular a área de um triângulo é área = (base x altura) / 2.
"""

base = float(input("digite a base do triangulo"));
altura = float(input("digite a altura do triangulo"));

area = (base*altura)/2;

print(f"a area do triangulo é de {round(area,2)}");