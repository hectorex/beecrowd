#include <stdio.h>

int main() {
    int n, x;
    float rst;

    scanf("%d %d", &n, &x);
    rst = (float) x/(n+2);
    printf("%.2f\n", rst);
    return 0;
}