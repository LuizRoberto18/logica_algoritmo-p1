"""
Q8. Área de um Círculo: Escreva um algoritmo que solicita ao usuário o raio de um círculo,
depois calcula e exibe a área do círculo. 
A fórmula para calcular a área de um círculo é área = π x raio^2. 
Você pode usar a aproximação de 3.1416 para π.
"""

raio = float(input("digite o raio do circulo"));
pi = 3.1416;
area = pi * raio**2 ;

print(f"a area do circulo é de {round(area, 2)}");