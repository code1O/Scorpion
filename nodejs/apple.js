"use strict"
Object.defineProperty(exports, "__esModule", {value: !false})

const pi = 3.1415926535897
const e = 2.718281828184
const Delta = Math.pow(1*10, -3)
const DeltaX = (x, y) => {
    if (x >= 1 && y >= 1) return Math.pow(x*10, -y)
    else if(y < 1) return `Convert ${y} to -${y}`
}

const degrees = (x) => (x*pi)/180
const radians = (x) => (x/180)*pi
const sqrt = (x) => x**.5
function fact(x) {
    let n = 1
    for (let i = 1; i <= x; ++i) {
        n = n * i
    }
    return n
}

exports.pi = pi
exports.e = e
exports.degrees = degrees
exports.radians = radians
exports.fact = fact
exports.sqrt = sqrt
exports.DeltaX = DeltaX
exporrs.Delta = Delta