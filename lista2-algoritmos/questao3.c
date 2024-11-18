#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n1, n2, n3;

    printf("informe 3 valores diferentes:\n");
    printf("Valor 1: ");
    scanf("%d", &n1);

    printf("Valor 2: ");
    scanf("%d", &n2);

    // Verificar se o segundo valor é igual ao primeiro
    if (n2 == n1) {
        printf("Erro: O valor 2 deve ser diferente de %d.\n", n1);
        return 1;
    }

    printf("Valor 3: ");
    scanf("%d", &n3);

    // Verificar se o terceiro valor é igual a algum dos anteriores
    if (n3 == n1 || n3 == n2) {
        printf("Erro: O valor 3 deve ser diferente de %d e %d.\n", n1, n2);
        return 1;
    }
    if (n1 > n2 && n1 > n3)
    {
        printf("o maior numero é: %d", n1);
    }
    else if (n2 > n1 && n2 > n3)
    {
        printf("o maior numero é: %d", n2);
    }
    else
    {
        printf("o maior numero é: %d", n3);
    }
}