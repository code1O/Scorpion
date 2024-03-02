# Matrix

````JavaScript
const { matrix } = require("scorpion/nodejs/_defdatas");

let matrix_variable = [
    [5,4,3,0,8],
    [1,6,3,2,9],
    [1,7,2,5,4]
]

let matrix_instance = new matrix(matrix_variable, 2);
matrix.instance.overwrite([5,5,0,8,1]);
console.log(matrix_instance.get("matrix"));
````

# Arrays

````JavaScript
const { theArray } = require("scorpion/nodejs/_defdatas")

````