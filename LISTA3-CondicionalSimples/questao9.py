"""
Q9. Elabore um algoritmo para que só possa autorizar a entrada na loja, 
aqueles que estão com a anuidade de associação em dia ou pagar o valor de 25 reais na entrada.
"""
print("= " * 10 + " autorizar a entrada " + "= "* 10);

anuidade = str(input("sua anuidade de associação está em dia? (S ou N)\n"));
if(anuidade == "S"):
    print("Acesso liberado");
else:
    taxa = str(input("deseja pagar o valor de 25 reais na entrada? (S ou N)\n"));
    if(taxa == "S"):
        print("Acesso liberado");
    else:
        print("Acesso negado!");