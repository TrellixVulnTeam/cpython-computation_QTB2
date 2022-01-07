#include <stdio.h>
int max(int x, int y) {
    return x > y ? x : y;
}

int main(void) {
    
    printf("Bonjour fabrice");

    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    /* Create conversion table using the equation C =(5/9) (F -32) */

    fahr = lower;
    while (fahr <= upper) {
        celsius = 5.0/9.0 * fahr - 32;
        printf("%3.0f \t%6.1f\n", fahr, celsius);
        fahr += step;
    }

    printf(max(10,20));
    

    return 0;
}