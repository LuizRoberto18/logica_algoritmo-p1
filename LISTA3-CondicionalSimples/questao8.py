'''
Q8. Elabore um algoritmo que solicita duas informações do usuário. 
A primeira, pergunta se possui bolsa família (S ou N), e a segunda, se possui mais de três filhos (S ou N). 
Se for contemplado pelo bolsa família e possuir mais de três filhos, 
deverá retornar Verdadeiro, significando que pode acessar à vaga de cotista.
'''

bolsa = str(input("possui bolsa família? (S ou N)\n"));
filhos  = str(input("possui mais de três filhos? (S ou N)\n"));

if(bolsa == "S" and filhos == "S"):
    print("pobre detectado com sucesso, vc tem acesso a vaga de cotista");
else:
    print("Você não bateu sua meta de pobreza, acesso a vaga de cota negado!");