#include <stdio.h>

int main() {
    int b, g;
    scanf("%d", &b);
    scanf("%d", &g);

    if (g%2 != 0) {
        g-=1;
    }
    if (b < g/2){
        printf("Faltam %d bolinha(s)\n", (g/2-b));
    }
    else{
        printf("Amelia tem todas bolinhas!\n");
    }

    return 0;
}