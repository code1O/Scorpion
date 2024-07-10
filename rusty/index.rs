#[allow(dead_code)]
#[allow(unused_variables)]

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

    pub fn sci_not(value: i32) -> String {
        let len_str_x = value.to_string().len();
        format!("{}(10)**{}", value, len_str_x)
    }
    pub fn logn(value: f64) -> f64 {
        let n = 10*100;
        n as f64*((value.powi(1/n))-1.0)
    }
}