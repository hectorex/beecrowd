#include <stdio.h>

int main() {

    int v[3];

    scanf("%d %d %d", &v[0], &v[1], &v[2]);
    float total = (float) v[0]/(v[1]+v[2]);
    printf("%.2f\n", total);
    return 0;
}