#include <stdio.h>

int main() {
    char v[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};    
    char i;

    scanf("%c", &i);
    for (int c = 0; c < sizeof(v); c++){
        printf("%d\n", c+1);
        if (v[c] == i){
            printf("%d\n", c+1);
            break;
        }
    }
    return 0;
}