#include <stdio.h>
#include "conversion.h"

int main() {
	double cm, inches;
	printf("How many inches (inch)?");
	if (scanf("%lf", & inches)) {
		cm = inchesToCm(inches);
		printf("%.2lf inches is %.2lf cm\n", inches, cm);
	}	else {
		printf("Invalid input. Please input valid floating point numbers. \n");
	}
	return 0;
}
