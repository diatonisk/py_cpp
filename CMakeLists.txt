cmake_minimum_required(VERSION 3.0.0)
project(py_cpp_add LANGUAGES CXX)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY $ENV{WORKSPACE}/py_cpp/core)

add_subdirectory(pybind11)
pybind11_add_module(py_cpp_add py_cpp/core/src/add.cpp)

target_compile_definitions(py_cpp_add
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})