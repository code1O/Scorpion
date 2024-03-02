
#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(unused_imports)]

/**
## `Handledatas`

Rust module for handling datas with essential functions.
As in python, it could work excellent for data science.

## Classes:

- **`Matrix`**

  Matrix data handling like overwriting values
  or iteration bewtween other matresses.

- **`Array`**

  Array data handling like creating another array
  inside or mathematical calculation.
*/
pub mod datas{

    pub struct Matrix {
        _matrix: Vec<Vec<u32>>,
        positional: usize,
    }

    impl Matrix {
        pub fn new(matrix: Vec<Vec<u32>>, positional: usize) -> Self {
            Matrix {
                _matrix: matrix,
                positional: positional,
            }
        }

        pub fn overwrite(&mut self, new_data_vector: Vec<u32>) {
            let position = self.positional - 1;
            if new_data_vector.len() > self._matrix[position].len() {
                panic!("{}", "Vector length must be same as matrix!");
            } else {
                self._matrix[position] = new_data_vector;
            }
        }

        /**
         * Create a new column with zeros inside
        */
        pub fn create_column(&mut self) {
            let new_values = vec![0; self._matrix[0].len()];
            self._matrix.push(new_values);
        }

        pub fn get(&mut self, type_data: &str) {}

        /**
        ## `Matrix.iterate`
        Iterate matrix values between first, second & third matrix
        and calculate the values depending the type of operation specified
        */
        pub fn iterate(&mut self, y_matrix: Vec<Vec<u32>>,
            z_matrix: Vec<Vec<u32>>, data_type: &str
        ) -> Vec<Vec<u32>> {
            let mut third_matrix_values = z_matrix;
            let (mut _matrix_x_values, mut _matrix_y_values) = (0, 0);
            for i in 0..(self._matrix.len()) {
                for j in 0..(self._matrix[self.positional].len()){
                    (_matrix_x_values, _matrix_y_values) = (self._matrix[i][j], y_matrix[i][j]);
                    match data_type {
                        "mult" => {
                            third_matrix_values[i][j] = _matrix_x_values * _matrix_y_values;
                        },
                        "add" => {
                            third_matrix_values[i][j] = _matrix_x_values + _matrix_y_values;
                        },
                        "div" => {
                            third_matrix_values[i][j] = _matrix_x_values / _matrix_y_values;
                        },
                        "subs" => {
                            third_matrix_values[i][j] = _matrix_x_values - _matrix_y_values;
                        }
                        _ => unreachable!()
                    };
                }
            }
            third_matrix_values
        }

        pub fn matrix(&self) -> &Vec<Vec<u32>> {
            &self._matrix
        }
    }

    pub struct Array {
        array: Vec<u32>,
        position: usize,
        empty_arr: Vec<u32>
    }
    impl Array {
        pub fn new(_array: Vec<u32>, _position: usize) -> Self {
            Array {
                array: _array,
                position: _position-1,
                empty_arr: vec![0]
            }
        }
        pub fn create_array_inside(&mut self) -> Vec<Vec<u32>> {
            let mut result = Vec::new();
            if !self.array.is_empty() {
                result.push(vec![*self.array.first().unwrap()]);
            }
            let transformed = self.array.clone();
            result.push(transformed);
            if self.array.len() > 1 {
                result.push(vec![*self.array.last().unwrap()]);
            }
            result
        }
        pub fn array(&self) -> &Vec<u32> {
            &self.array
        }
        pub fn bignotation(&mut self, vector: Vec<u32>,notation_type: &str) -> usize {
            fn lognotation (vector: Vec<u32>, value_to_find: u32) -> usize {
                let (left, right, mut _middle) = (0, vector.len(), 0);
                let mut result = 0;
                for i in left..=right {
                    _middle = ((left + right)/2) as usize;
                    if vector[_middle] == value_to_find {
                        result = _middle;
                    } else if vector[_middle] < value_to_find {
                        result = _middle + 1;
                    } else if vector[_middle] > value_to_find {
                        result = _middle - 1;
                    }
                }
                result
            }
            match notation_type {
                "O(log)" => {
                    lognotation(vector, self.position as u32)
                },
                "O(1)" => {
                    vector[self.position] as usize
                },
                _ => unreachable!()
            }
        }
    }
}