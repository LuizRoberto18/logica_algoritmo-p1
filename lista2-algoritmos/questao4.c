#include <stdio.h>
#include <stdlib.h>

int main(){
    int n1,n2,soma;

    printf("digite 2 valores:\n");

    printf("valor 1:\n");
    scanf("%d", &n1);

    printf("valor 2:\n");
    scanf("%d", &n2);

    soma = n1+ n2;

    printf("a soma é: %d\n", soma);

    if(soma > 20){
        soma += 8;
        printf("a soma é maior que vinte por isso foi adicionado mais 8, valor final: %d", soma);
    }
    if(soma <= 20){
        soma -= 5;
        printf("a soma é menor que vinte por isso foi subtraido 5, valor final: %d", soma);
    }

    return 0;
}