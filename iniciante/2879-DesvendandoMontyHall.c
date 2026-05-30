#include <stdio.h>

int main() {
    int n,total = 0,val;
    scanf("%d", &n);

    for (int i = 1; i<=n; i++) {
        scanf("%d", &val);
        if (val != 1) {
            total++;
        }
    }

    printf("%d\n",total);

    return 0;
}