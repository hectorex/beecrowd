#include <stdio.h>

int main() {
    int l,c, rst;

    scanf("%d", &l);
    scanf("%d", &c);

    if (l%2 == 0 && c%2 == 0) {
        rst = 1;
    }
    else if (l%2 == 1 && c%2 == 0) {
        rst = 0;
    }
    else if (l%2 == 0 && c%2 == 1) {
        rst = 0;
    }
    else if (l%2 == 1 && c%2 == 1) {
        rst = 1;
    }

    printf("%d\n",rst);

    return 0;
}