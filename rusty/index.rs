#[allow(dead_code)]

pub mod mathfuns{
    pub const PI: f64 = 3.14159265;
    pub const E: f64 = 2.7182818284;

    pub fn fact(x: i32) -> f64 {
        let mut number_factorial = 1;
        for i in 1..=x {
            number_factorial*=i;
        }
        number_factorial.into()
    }
    pub fn degrees<T: Into<f64>>(x: T) -> f64 {
        let x: f64 = x.into();
        (x * PI)/180.0
    }
    pub fn radians<T: Into<f64>>(x: T) -> f64 {
        let x: f64 = x.into();
        (x * 180.0)/PI
    }

    pub fn sqrt<T: Into<f64>>(x: T) -> f64 {
        let x: f64 = x.into();
        x.powf(0.5)
    }
}