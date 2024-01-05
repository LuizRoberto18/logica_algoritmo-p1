'''
Q6. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, 
mas que só permite compras à vista.
'''
print("="*10 + " sistema de compra " + "="*10 + "\n");
print("="*6 + " Produtos " + "="*6 + "\n");

print("1. Mato - R$ 20,00\n");
print("2. Terra - R$ 25,00\n");
print("3. Semente - R$ 15,00\n");
print("4. Planta - R$ 45,00\n");

pedido = int(input("para realizar a compra escolha o numero do produto\n"));

print("="*6 + " Forma de pagamento " + "="*6 + "\n");

print("1. á vista\n");
print("2. Parcelado\n");
print("3. Cu\n");

formPagamento = int(input("para finalizar a compra, selecione a forma de pagamento\n"));
pagamento = "";
item = "";

if(formPagamento == 1):
    pagamento = "á vista";
elif(formPagamento == 2):
    pagamento = "Parcelado";
elif(formPagamento == 3):
    pagamento = "Cu";

if(pedido == 1):
    item = "Mato";
elif(pedido == 2):
    item = "Terra";
elif(pedido == 3):
    item = "Semente";
elif(pedido == 4):
    item = "Planta";

if(formPagamento == 1):
    print("Compra realizada com sucesso: pedido: {}, forma de pagamento: {}".format(item,pagamento));
else:
    print("Erro ao finalizar compra: Método de pagamento invalido, {} está indisponivel no momento!".format(pagamento));