#include <stdio.h>

int main() {
    int v[3];
    scanf("%d %d %d", &v[0], &v[1], &v[2]);
    if (v[0] - v[1] == 0 || v[0] - v[2] == 0 || v[1]-v[2] == 0) {
        printf("S\n");
    }

    else if(v[0] + v[1] == v[2] || v[0] + v[2] == v[1] || v[1]+v[2] == v[0]){
        printf("S\n");
    }

    else {
        printf("N\n");
    }
    return 0;
}