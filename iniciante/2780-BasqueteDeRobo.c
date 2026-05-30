#include <stdio.h>    

int main() {
    int num, pnts;
    scanf("%d", &num);

    if (num <= 800){
        pnts = 1;
    }
    else if (num <= 1400){
        pnts = 2;
    }
    else if (num <= 2000){
        pnts = 3;
    }
    printf("%d\n", pnts);
    return 0;
}