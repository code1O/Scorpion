"use strict";

Object.defineProperty(exports, "__esModule", {value: true});

const { map } = require("mathjs");

class matrix{
    constructor(matrix, positional=1) {
        this.matrix = matrix;
        this.positional = positional-1;
        this.new_values = [0];
    }
    overwrite(value) {
        for (let i = 0; i <= this.value.length; ++i) value = value[i];
        this.matrix[this.positional] = value;
        return this.matrix;
    }
    get(rtype) {
        let MapArrColumn = this.array[this.positional].map(x => x);
        switch (rtype) {
            case "column":
                return MapArrColumn;
            case "matrix":
                return this.matrix;
            case "row":
                for (let value of this.matrix){
                    this.new_values.push(value[this.positional]);
                }
                return this.new_values;
        }
    }
}

class theArray {
    constructor(array, position) {
        this.array = array;
        this.position = position - 1;
        this.empty_arr = [0];
    }
    createArrayInside() {
        let n = 0;
        let values = this.array.map(x => x);
        const newArrayInside = this.empty_arr.splice(1, 0, values);
        this.array.splice(this.position, 0, newArrayInside);
        for (let i = 0; i<(this.array.length)-1; ++i) {
            n = n * i;
            this.array[this.position].splice(0, 0, n);
        }
        this.array[this.position]
        .splice(1, this.array.length, ...newArrayInside);
        return this.array;
    }
}

exports.theArray = theArray;
exports.matrix = matrix;
