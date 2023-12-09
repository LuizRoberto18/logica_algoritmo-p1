"""
Q6. Escreva um algoritmo que solicita ao usuário uma temperatura em graus Celsius e a converte para graus Fahrenheit e Kelvin. 
Use as fórmulas Fahrenheit = Celsius * 1.8 + 32 e Kelvin = Celsius + 273.15 para realizar as conversões.
"""

celsius= float(input("informe quantos graus celsius deseja converter"));

fahrenheit = (celsius * 1.8) + 32;
Kelvin = celsius + 273.15;

print(f"{celsius}c° equivale a {round(fahrenheit, 2)}f°");
print(f"{celsius}c° equivale a {round(Kelvin,2)}k°");