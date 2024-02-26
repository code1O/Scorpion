
# Matrix
````rust
#[path="scorpion/rusty/handledatas.rs"]
mod handledatas;
use handledatas::datas;

fn main() {
    let mut matrix: Vec<Vec<u32>> = vec![
        vec![1,2,3,4,5],
        vec![5,6,7,8,9],
        vec![7,8,9,10,11]
    ];
    let mut matrix_instance = datas::Matrix::new(matrix, 2);

    // Modify with new values the column #2 from `matrix`
    matrix_instance.overwrite(vec![10,20,21,25,30]);

    // Return `matrix` with the new values
    println!("{:?}", matrix_instance.matrix());
}
````

# Arrays

````rust
#[path="scorpion/rusty/handledatas.rs"]
mod handledatas;
use handledatas::array;
````