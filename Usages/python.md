**Import the library**

````python
import scorpion.python as scorpion
````

# Matrix

````python
matrix = [
    [2,4,6,8],
    [3,6,9,12],
    [4,8,12,16]
]

matrix_instance = scorpion.matrix(matrix, 2)
matrix_instance.overwrite([6,1,8,6])

# Create multiple matresses
new_matresses = scorpion.matrix.create_multiple(4,4,"x; y; z")
matrix_instance_y = scorpion.matrix(new_matresses, 1)
print(matrix_instance.get("matrix"), matrix_instance_y.get("matrix"))

# pairing matrix
# Conjunt notation in mathematics
# (a,b),(b,c),(c,d)

print(matrix_instance.pair("x"))
# Should produce: [2,3,4]

print(matrix_instance.pair("y"))
# Should produce: [4,6,8]
````

# Arrays

````python
array = [0,1,3,4,6,24,32,86]
array_y = [array[-1], 12, array[3], 52]

# Math calculus
math_instance = scorpion.matharray(array, 1)
math_instance.maxSum()
math_instance.mult(10)
print(math_instance)

# Data handling
instance_array = scorpion.Array(array, 1)
instance_array.Reverse()
instance_array.createArayInside()
position_value = instance_array.bignotation("O(log n)", 6) #could be any value instead 6
union, intersect = instance_array.union(array_y), \
                  instance_array.intersect(array_y)
print(instance_array, position value, [union, intersect])
````

# Calculating equations

![equation](https://latex.codecogs.com/png.image?\dpi{110}\left(\frac{\partial&space;f}{\partial&space;x}(2x^2)\right)\frac{\psi(x)\Gamma(x&plus;1)}{\Gamma'(x&plus;1)}\psi\left(\frac{x}{y}&plus;1\right))

```python
from python import (derivative, gamma, psi)
n,m = 5, 2
d_gamma = 1
dx = derivative(2,x=n,power=2)
gamma_recursive = gamma(n, recursive=True)
psi_recursive = psi(n,m,recursion=True)
psi_normal = psi(n)
calculus = dx*((psi_normal*gamma_recursive)/d_gamma)
print(calculus*psi_recursive)
```