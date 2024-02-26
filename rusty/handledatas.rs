#[allow(dead_code)]

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

        pub fn overwrite(&mut self, new_data_vec: Vec<u32>) {
            let position = self.positional - 1;
            if new_data_vec.len() > self._matrix[position].len() {
                panic!("{}", "Vector length must be same as matrix!");
            } else {
                self._matrix[position] = new_data_vec;
            }
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
    }
}