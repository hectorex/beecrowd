#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        int c;
        scanf("%d", &c);
        printf("resposta %d: %d\n", i+1, c);
    }
    return 0;
}