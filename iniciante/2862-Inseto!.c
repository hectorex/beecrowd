#include <stdio.h>
#include <string.h>

int main() {
    int n, val;
    char rsp[15];
    strcpy(rsp, "Inseto!");
    scanf("%d", &n);

    for (int i = 0; i<n; i++) {
        scanf("%d", &val);
        if (val > 8000){
            strcpy(rsp, "Mais de 8000!");
        }
        printf("%s\n", rsp);
        strcpy(rsp, "Inseto!");
    }

    return 0;
}