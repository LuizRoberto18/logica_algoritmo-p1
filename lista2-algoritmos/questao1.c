
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c;

    printf("vamos formar um triangulo informados os lados a,b e c:\n");
    printf("insira o valor de A: ");
    scanf("%d", &a);
    if (a <= 0) {
        printf("O valor de A deve ser maior que zero.\n");
        return 1;
    }
    printf("insira o valor de B: ");
    scanf("%d", &b);
    if (b <= 0) {
        printf("O valor de B deve ser maior que zero.\n");
        return 1;
    }
    printf("insira o valor de C: ");
    scanf("%d", &c);
    if (c <= 0) {
        printf("O valor de C deve ser maior que zero.\n");
        return 1;
    }

    if((a < (b+c)) && (b < (a+c)) && (c <( b+a))){
        printf("Você formou um triangulo");
    }else{
        printf("Não formamos um triangulo, tente novamente.");
    }

    return 0;
}