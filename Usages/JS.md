
**Import the library**
````JavaScript
"use strict";
Object.defineProperty(exports, "__esModule", {value: true})
````

# Matrix

````JavaScript
const datas = require("scorpion/nodejs/_defdatas");

let matrix = [
    [5,4,3,0,8],
    [1,6,3,2,9],
    [1,7,2,5,4]
]

let matrix_instance = new matrix(matrix, 2);
matrix.instance.overwrite([5,5,0,8,1]);
console.log(matrix_instance.get("matrix"));
````