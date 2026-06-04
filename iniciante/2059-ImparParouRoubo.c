#include <stdio.h>

int main() {
    int p1, n1, n2, r, a;
    scanf("%d %d %d %d %d", &p1, &n1, &n2, &r, &a);
    if (r == 1 && a == 0){
        printf("Jogador 1 ganha!\n");
    }
    else if (r == 1 && a == 1){
        printf("Jogador 2 ganha!\n");
    }
    else if (r == 0 && a == 1) {
        printf("Jogador 1 ganha!\n");
    }
    else if (p1 == 1){
        if ((n1+n2)%2 == 0) {
            printf("Jogador 1 ganha!\n");
        }
        else {
            printf("Jogador 2 ganha!\n");
        }
    }
    else if (p1 == 0){
        if ((n1+n2)%2 == 0) {
            printf("Jogador 2 ganha!\n");
        }
        else {
            printf("Jogador 1 ganha!\n");
        }
    }
    return 0;
}