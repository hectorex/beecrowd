#include <stdio.h>

int main() {
    int s, t, f, arrive;

    scanf("%d %d %d", &s, &t, &f);

    if (s+t+f >= 24){
        arrive = (s+t+f)-24;
    }
    else if (s+t+f < 0){
        arrive = (s+t+f)+24;
    }
    else if (s+t+f == 0) {
        arrive = 0;
    }
    else {
        arrive = s+t+f;
    }
    printf("%d\n", arrive);
    return 0;
}