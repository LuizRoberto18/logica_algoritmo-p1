"""
Q4. Escreva um algoritmo que leia a nota de 3 estudantes
e retorne a média das notas.

"""

nota1 = float(input("digite a nota 1"));
nota2 = float(input("digite a nota 2"));
nota3 = float(input("digite a nota 3"));

media = (nota1 +nota2+nota3)/3;

print(f"a media de notas é {round(media, 2)}");