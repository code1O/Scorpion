#include <cmath>
#include <vector>
#include <iostream>
#include "DEFINE.h"

long sindeg(long value) {
    long x = toDeg(value);
    long res1 = x-pow(x, 3)/factorial(3)+pow(x,5)/factorial(5);
    return res1-pow(x, 7)/factorial(7);
}

long cosdeg(long value) {
    long x = toDeg(value);
    long res1 = 1-pow(x, 2)/factorial(2)+pow(x, 4)/factorial(4);
    return res1-pow(x, 6)/factorial(6);
}