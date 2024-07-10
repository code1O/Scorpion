
# Matrix
````rust
#[path="scorpion/rusty/handledatas.rs"]
mod handledatas;
use handledatas::datas;

fn main() {
    let (_matrix_x, _matrix_y, _matrix_z) = (
    vec![
        vec![1,2,3,4,5],
        vec![4,5,6,7,8],
        vec![5,6,7,8,9]
    ],
    vec![
        vec![5,9,12,4,6],
        vec![6,7,12,33,11],
        vec![80,100,20,132,55]
    ],
    vec![
        vec![0,0,0,0,0],
        vec![0,0,0,0,0],
        vec![0,0,0,0,0]
    ]);
    let mut matrix_instance = datas::Matrix::new(_matrix_x, 2);


    fn Modify_matrix() -> Vec<Vec<u32>> {
        // Modify with new values the column #2 from `matrix`
        matrix_instance.overwrite(vec![10,20,21,25,30]);
        // Iterate between matresses `_matrix_y` and `_matrix_z`
        matrix_instance.iterate(_matrix_y, _matrix_z, "add");
        // You can input 'mult' or other instead 'add'
        _matrix_x
    }

    print!("{:?}", Modify_matrix());
}
````

# Arrays

````rust
#[path="scorpion/rusty/handledatas.rs"]
mod handledatas;
use handledatas::array;

let (_array_x, _array_x_copy) = (
    vec![110, 240, 315, 450, 550], vec![110, 240, 315, 450, 550]
);

let mut array_instance = Array::new(_array_x,);
let bignot_log = array_instance.bignotation(_array_x_copy, "O(log)"));
let bignot_consistent = array_instance.bignotation(_array_x_copy, "O(1)");

let bignot_message = format!("O(log): {}  O(1): {}",
bignot_log, bignot_consistent);

let array_with_array_inside = array_instance.create_array_inside();
println!("{:?}", bignot_message);
println!("{:?}", array_with_array_inside);
````