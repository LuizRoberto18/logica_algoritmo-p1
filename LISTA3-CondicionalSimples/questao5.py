"""
Q5. Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do usuário, e a senha. 
Depois, pede que o usuário confirme novamente a senha. 
O sistema deverá verificar se as senhas digitadas são iguais. 
Se forem iguais, informar que o cadastro está correto. 
Se não forem iguais, informar que o cadastro não foi realizado porque as senhas não conferem.
"""
print("="*10 + " cadastro de usuário " + "="*10);
usuario = str(input("digite nome do usuário:\n"));
senha =str(input("digite a senha:\n"));
confir = str(input("confirme a senha:\n"));
if(senha == confir):
    print("Usuário {} cadastrado com sucesso!".format(usuario));
else:
    print("Erro ao cadastrar usuário: a senha não confere");