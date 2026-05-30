#include <stdio.h>

int main() {
    int l, c, tipo1, tipo2;
    scanf("%d\n", &c);
    scanf("%d", &l);

    tipo1 = (l*c)+((l-1)*(c-1));
    tipo2 = ((l-1)*2)+((c-1)*2);

    printf("%d\n", tipo1);
    printf("%d\n", tipo2);
}

