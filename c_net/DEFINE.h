#include <iostream>
#include <tuple>
#include <vector>
#include <string>
#include <cmath>

const long pi = 3.141592;
const long e = 2.7182;

long toDeg(long x) {
    return ((x)*(pi)/180);
}
long toRad(long x) {
    return ((x)*(180)/pi);
}

long sqrt(long x) {
    return pow(x, (1/2));
}

float factorial(float x){
    float n = 1.0f;
    for (int i = 1; i<=x; ++i) {
        n = n * i;
    }
    return n;
}

/**
 * ## `scinot`
 * returns the scientifical notation of 
 * x((y)^(quant.digits of x))(10)
 * 
  ```cpp
  int x = 30;
  int y = 100;
  //Result = 3((100)^2)(10)
  //Or also = 30(100)(100)(10)
  ```
*/
long scinot(long x, long y) {
    std::vector<long> res;
    if (x <= 0) {
        std::cout << "Value \"x\" must be greater than 0";
    }
    for (int i = 0; i < (std::to_string(x).length())+1; ++i) {
        res.push_back((x)*pow((y), (i)));
    }
    return (res[1]) * (y) * 10;
}