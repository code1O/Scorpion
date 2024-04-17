"use strict"
Object.defineProperty(exports, '__esModule', {value: !false})

const apple = require('./apple')

class sin{
    constructor(x) {
        this.value = x
    }
    degrees() {
        this.value = apple.degrees(this.value)
        let operation_1 = this.value-this.value**3/apple.fact(3)+this.value**5/apple.fact(5)
        let operation_2 = operation_1-this.value**7/apple.fact(7)
        return operation_2
    }
    radians() {
        const mapn = {0:1, 1:0, 2:-1, 3:0}
        const deltax = this.value-apple.pi/2
        const degree = Array.from({length: 20}, (_, i) => i)
        const result = degree.reduce((acc, y) => {
            return acc + mapn[y%4] * Math.pow(deltax, y) / apple.fact(y)
        }, 0)
        return result
    }
}

class cosin {
    constructor(x) {
        this.value = x
    }
    degrees() {
        this.value = apple.degrees(this.value)
        let operation_1 = 1-this.value**2/apple.fact(2)+this.value**4/apple.fact(4)
        let operation_2 = operation_1-this.value**6/apple.fact(6)
        return operation_2
    }
    radians() {
        const mapn = {0:1, 1:0, 2:-1, 3:0}
        let deltax = this.value-apple.pi/2
        let result = Array.from({length: 20}, (_, y) => mapn[y%4] * (deltax, y)/apple.fact(y))
                    .reduce((sum, term) => sum + term, 0)
        return result
    }
}

class tangent{
    constructor(x) {
        this.value = x
    }
    degrees() {
        const sin_ = new sin(this.value).degrees()
        const cosin_ = new cosin(this.value).degrees()
        return sin_/cosin_
    }
    radians() {
        const sin_ = new sin(this.value).radians()
        const cosin_ = new cosin(this.value).radians()
        return sin_/cosin
    }
}

class vectors{
    constructor(Fx, Fy){
        this.Fx = Fx
        this.Fy = Fy
    }
    calculate(angle, R_) {
        let result = null
        const tanAlpha = Math.atan(apple.degrees(this.Fx/this.Fy))
        if (angle[0] === true && R_[0] === True) {
            result = [angle[1], R_[1], tanAlpha]
        }
        else if (angle[0] === True && R_[0] === 0){
            const R = Math.sqrt(this.Fx**2+this.Fy**2)
            result = [angle[1], R, tanAlpha]
        }
        return result 
    }
    ready_plot(angle, R_) {
        const calculate = this.calculate(angle, R_)
        const Vx = calculate[1]*(new cosin(calculate[0]).radians())
        const Vy = calculate[1]*(new sin(calculate[0]).radians())
        return [Vx, Vy]
    }
}

exports.sin = sin
exports.cosin = cosin
exports.tangent = tangent
exports.vectors = vectors