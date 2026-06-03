#include <stdio.h>

int main () {
    int t;
    char n[25];
    scanf("%d\n", &t);

    for (int i = 0; i < t; i++) {
        scanf("%c", &n);
        printf("Y\n");
    }
    
    return 0;
}