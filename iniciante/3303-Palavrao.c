#include <stdio.h>
#include <string.h>

int main() {
    char text[20];
    scanf("%s", &text);

    if (strlen(text) >= 10) {
        printf("palavrao\n");
    }
    else {
        printf("palavrinha\n");
    }

    return 0;
}