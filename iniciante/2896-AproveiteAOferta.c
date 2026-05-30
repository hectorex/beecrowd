#include <stdio.h>

int main(){
    int t, v[2], total;
    scanf("%d", &t);
    for (int i = 1; i<=t; i++) {
        scanf("%d %d", &v[0], &v[1]);
        total = (v[0] % v[1]) + (v[0] / v[1]);
        printf("%d\n", total);
    }

    return 0;
}