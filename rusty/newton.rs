#[path="index.rs"]
mod index;

#[path="handledatas.rs"]
mod datas;

#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(unused_imports)]
#[allow(unused_assignments)]
#[allow(unused_mut)]

/**
# `mathops`
Essential mathematical operations for calculus in projects or scripts

## Operations

- **`FindFactor`**

  Find the factorization for two numbers,
  e.g. the factorization for `x^2+7x-12`
  is equal to `(3)(-3)/(4)(-3)`

- **`Factor`**
   
   Return the factorization for any numbers, e.g. `(3)(-3)/(4)(-3)`
   will return `3` & `4`.

- **`Integral`**
  
  Return the integration of a function.

  Types of integration: Integration by factorization

## Some important guide

### Factorizing

  The factorization implies `Factor` & `FindFactor`.

  The factorization could be automatic or manual

  - Automatic

    ```rust
    #[path="rusty/mod.rs"]
    mod rusty;
    use rusty::newton::mathops;
    fn main() {
        let (x, y, my_type) = (7, -12, "division");
        let mut factor_instance = mathops::FindFactor(x, y);
        
        // Binomial, return for top calculation
        let for_top_bin = factor_instance.double_top();
        
        // Binomial, return for bottom calculation
        let for_bott_bin = factor_instance.double_bottom();
        
        // Binomial, return for both calculation
        let for_both_bin = factor_instance.double_both(my_type);
    }
    ```
*/
pub mod mathops{

    use std::result;

    use super::datas::datas::{self, Array};
    use super::index::mathfuns::{self, fact, sqrt, logn};
    
    pub struct Factor {
        tuple_variables: Vec<i32>,
    }

    impl Factor {
        pub fn new(vector: Vec<i32>) -> Self {
            let (x1, y1, x2, y2) = (vector[0], vector[1], vector[2], vector[3]);
            Self {
                tuple_variables: vec![x1, y1, x2, y2],
            }
        }

        pub fn double_both(&mut self) -> Vec<i32> {
            let (x1_value, y1_value, x2_value, y2_value) = (
                self.tuple_variables[0], self.tuple_variables[1],
                self.tuple_variables[2], self.tuple_variables[3]
            );

            fn one_version(x1_value: i32, y1_value: i32) -> i32 {
                if x1_value == -x1_value && y1_value == x1_value {
                    x1_value
                } else if x1_value == x1_value && y1_value == -x1_value {
                    y1_value
                } else {
                    y1_value
                }
            }

            fn two_version(x1_value: i32, y1_value: i32, x2_value: i32, y2_value: i32) -> i32 {
                if x2_value == -x1_value && y2_value == y1_value {
                    x2_value
                } else if x2_value == x1_value && y2_value == -y1_value {
                    y2_value
                } else {
                    y2_value
                }
            }

            vec![
                one_version(x1_value, y1_value), 
                two_version(x1_value, y1_value, x2_value, y2_value)
            ]
        }
        pub fn double_top(&mut self) -> Vec<i32> {
            let (x_value, y_value, z_value) = (
                self.tuple_variables[0], self.tuple_variables[1],
                self.tuple_variables[2]
            );
            pub fn some(x_value: i32, y_value: i32) -> i32 {
                if y_value == -x_value {
                    x_value
                }
                else if y_value == x_value {
                    y_value
                }
                else {
                    panic!("Values must be acceptable")
                }
            }
            vec![some(x_value, y_value), z_value]
        }
        pub fn double_bottom(&mut self) -> Vec<i32> {
            let (x_value, y_value, z_value) = (
                self.tuple_variables[0], self.tuple_variables[1],
                self.tuple_variables[2]
            );
            fn some(y_value: i32, z_value: i32) -> i32 {
                if z_value == -y_value {
                    y_value
                }
                else if z_value == y_value {
                    z_value
                }
                else {
                    panic!("Values must be acceptable")
                }
            }
            vec![x_value, some(y_value, z_value)]
        }

    }

    pub struct FindFactor {
        x: i32,
        y: i32,
    }
    
    impl FindFactor {
        pub fn new(x: i32, y: i32) -> Self {
            Self { x, y }
        }
    
        pub fn double_both(&self, rtype: &str) -> Result<f64, Vec<f64>> {
            let (mut n_variable, mut x_variable) = (0,0);
            for i in 0..(((self.x as f64).sqrt()).round() as i32 + 1) {
                for j in 0..(((self.y as f64).sqrt()).round() as i32 + 2) {
                    (n_variable, x_variable) = (i, j);
                }
            }
            if x_variable > 5 || x_variable == 5 {
                x_variable = x_variable-2;
            } else {
                x_variable = x_variable
            }
            let mult = x_variable * n_variable;
            
            let (rtop, rbott) = (
                vec![mult / x_variable, mult / n_variable],
                vec![mult / n_variable-1, -(mult /n_variable-1)],
            );

            let mult_bott: i32 = rbott[0] * rbott[1];
            let mult_top: i32 = rtop[0] * rtop[1];
            match rtype {
                "division" => {
                    let result = mult_bott as f64 / mult_top as f64;
                    Ok(result)
                },
                "top" => {
                    let result: Vec<f64> = vec![rtop[0] as f64, rtop[1] as f64];
                    Ok(result.into_iter().fold(0.0, |acc, x_variable| acc + x_variable))
                },
                "bottom" => {
                    let result: Vec<f64> = vec![rbott[0] as f64, rbott[1] as f64];
                    Ok(result.into_iter().fold(0.0, |acc, x_variable| acc + x_variable))
                }
                _ => Err(vec![0.0, 0.0])
            }
        }
        pub fn double_top(&mut self) -> f64{
            let mut x_value = 0;
            for i in 0..((sqrt(self.x as f64)).round() as i32 + 2) {
                x_value = i;
            }
            if self.y == 1 || self.y > 1 {
                x_value as f64
            }
            else {
                panic!("Failed to execute it!");
            }
        }
        pub fn double_bottom(&mut self) -> i32 {
            let (mut _x_identifier, mut _y_identifier) = (0,0);
            for i in 0..((sqrt(self.x as f64)).round() as i32) {
                for j in 0..((sqrt(self.x as f64)).round() as i32 +2){
                    (_x_identifier, _y_identifier) = (i, j);
                }
            }
            let result = _x_identifier * _y_identifier;
            self.x / result
        }

    }
    pub struct Sin {
        x_value: i32
    }
    impl Sin {
        pub fn new(value: i32) -> Self {
            Sin {
                x_value: value
            }
        }
        pub fn degrees(&mut self) -> f64 {
            let x: f64 = mathfuns::degrees(self.x_value);
            let result: f64 = x-x.powf(3.0)
            /fact(3)+x.powf(5.0)/fact(5)-x.powf(7.0)/fact(7);
            result
        }
        pub fn radians(&mut self) -> f64 {
            let x = self.x_value as f64;
            let (sin_x, _) = x.sin_cos();
            sin_x
        }
    }
    pub struct Cosin {
        x_value: i32
    }
    impl Cosin {
        pub fn new(value: i32) -> Self {
            Cosin {
                x_value: value
            }
        }
        pub fn degrees(&mut self) -> f64{
            let x: f64 = mathfuns::degrees(self.x_value);
            let result: f64 = 1.0-x.powf(2.0)
            /fact(2)+x.powf(4.0)/fact(4)-x.powf(6.0)/fact(6);
            result
        }

        pub fn radians(&mut self) -> f64 {
            let x: f64 = self.x_value as f64;
            let cosin_x = x.cos();
            cosin_x
        }
    }
    pub struct Tangent {
        value: i32,
    }
    impl Tangent {
        pub fn new(x_value: i32) -> Self {
            Tangent {
                value: x_value
            }
        }
        pub fn degrees(&mut self) -> f64 {
            let result: f64 = Sin::new(self.value).degrees()
            / Cosin::new(self.value).degrees();
            result
        }
        pub fn radians(&mut self) -> f64 {
            let result: f64 = Sin::new(self.value).radians()
            / Cosin::new(self.value).radians();
            result
        }
    }
    pub struct IntegralDefined {
        b_value: f64, 
        a_value: f64, 
        cvalues: Vec<f64>
    }
    impl IntegralDefined {
        pub fn new(b: f64, a: f64, cvalues: Vec<f64>) -> Self {
            Self {
                b_value: b,
                a_value: a,
                cvalues: cvalues
            }
        }
        ///
        /// **Integrate function by factorizing**
        /// ```rust
        /// #[path="rusty/mod.rs"]
        /// mod rusty;
        /// use rusty::newton::mathops;
        /// fn main() {
        ///   let (b, a, c_values) = (4, 0, vec![1, 2*1^2-2]);
        ///   let int_instance = mathops::IntegralDefined::new(b, a, c_values);
        ///   print!("{:?}", int_instance.fact());
        /// }
        /// ```
        /// 
        pub fn fact(&mut self) -> f64 {
            fn convert(result: Result<f64, Vec<f64>>) -> Vec<f64> {
                match result {
                    Ok(value) => vec![value],
                    Err(vec) => vec
                }
            }
            let (b, a) = (self.b_value, self.a_value);
            let (cval_a, cval_b) = (self.cvalues[0] as i32, self.cvalues[1] as i32);
            let factor_instance = FindFactor::new(cval_a, cval_b)
                                                        .double_both("top");

            let res  = convert(factor_instance);
            let (x_0, x_1) = (res[0], res[1]);

            let fx = vec![x_1 * b, x_0 * a];
            let calculus_b = (cval_a as f64 / fx[0]) * logn(fx[0]);
            let calculus_a = (cval_b as f64 / fx[1]) * logn(fx[1]);

            calculus_b - calculus_b
        }
    }
}
