#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <algorithm>

template <typename Type>

class Matrix{
    public:
    std::vector<std::vector<Type>> matrix_ptr;
    int positional;

    Matrix (const std::vector<std::vector<Type>> _matrix, int position): matrix_ptr(_matrix), positional(position-1) {}

    std::vector<std::vector<Type>> overwrite(const std::vector<Type> value) {
        if (positional < 0 || positional > matrix_ptr.size()) std::cerr << "Value not supported!";
        else if (value.size() > matrix_ptr[positional].size()) std::cerr << "Size mismatch!";
        std::vector<std::vector<Type>> newMatrix = matrix_ptr;
        newMatrix[positional] = value;
        return newMatrix;
    }
};

template <typename Type>

class Array{
    public:
    std::vector<Type> array_ptr;
    int positional;
    Array(const std::vector<Type> _array, const int position): array_ptr(_array), positional(position){}

};