#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d\n", &n);
    char text1[7];
    char text2[7];
    for (int i = 0; i<n; i++) {
        scanf("%s", &text1);
        scanf("%s", &text2);

        if (strcmp(text1, "ataque") == 0 && strcmp(text2, "ataque") == 0) {
            printf("Aniquilacao mutua\n");
        }
        else if (strcmp(text1, "ataque") == 0) {
            printf("Jogador 1 venceu\n");
        }
        else if (strcmp(text2, "ataque") == 0) {
            printf("Jogador 2 venceu\n");
        }
        else if (strcmp(text1, "pedra") == 0 && strcmp(text2, "pedra") == 0) {
            printf("Sem ganhador\n");
        }
        else if (strcmp(text1, "papel") == 0 && strcmp(text2, "papel") == 0) {
            printf("Ambos venceram\n");
        }
        else if (strcmp(text1, "papel") == 0 && strcmp(text2, "pedra") == 0) {
            printf("Jogador 2 venceu\n");
        }
        else if (strcmp(text1, "pedra") == 0 && strcmp(text2, "papel") == 0) {
            printf("Jogador 1 venceu\n");
        }
    }

    return 0;
}