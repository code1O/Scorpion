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