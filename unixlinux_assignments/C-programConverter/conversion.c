/* util.c */
#include "conversion.h"

const double INCHES_IN_CM =  2.54;

double cmToInches(double cm) {
	return cm/INCHES_IN_CM;
}

double inchesToCm(double inches) {
	return inches*INCHES_IN_CM;
}
