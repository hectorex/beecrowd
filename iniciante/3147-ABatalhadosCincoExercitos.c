#include <stdio.h>

int main() {
    int H, E, A, O, W, X, good, evil;

    scanf("%d %d %d %d %d %d", &H, &E, &A, &O, &W, &X);
    good = H+E+A+X;
    evil = O+W;

    if (good >= evil){
        printf("Middle-earth is safe.\n");
    }
    else {
        printf("Sauron has returned.\n");
    }
    return 0;
}