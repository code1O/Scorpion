#[path="index.rs"]
mod index;

#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(unused_assignments)]

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

## Some important guide

### Factorization

  The factorization implies `Factor` & `FindFactor`.

  There's many options for return the result of the factorization,
  If the factorization is binomial use `double_both`,
  else if the factorization is monomial instead in the top use `double_top`,
  else if the factorization is binomial instead in the bottom use `double_bottom`.
*/
pub mod mathops{

    use super::index::mathfuns::{self, fact, sqrt};
    
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

    pub struct CalculateVec {
        fx: Result<i32, f64>,
        fy: Result<i32, f64>
    }
    impl CalculateVec {
        pub fn new(fx: Result<i32, f64>, fy: Result<i32, f64>) -> Self {
            CalculateVec {
                fx: fx,
                fy: fy
            }
        }
        
    }
}