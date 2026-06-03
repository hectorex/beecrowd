#include <stdio.h>
#include <math.h>

int main(){
    double a, b, rsp, pib;
    pib = 100.0;
    scanf("%lf %lf", &a, &b);

    rsp = (1 + a/100) * (1 + b/100) * 100 - 100;

    printf("%.6lf\n", rsp);
    return 0;
}