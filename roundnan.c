#include <stdio.h>
#include <math.h>

/*
 * In Java, Math.Round(Math.NaN) = 0.
 *
 * Is it the same way in C?
 */

int main() {

	printf("%f\n", round(NAN));

	return 0;
}
