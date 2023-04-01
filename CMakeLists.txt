cmake_minimum_required(VERSION 3.0.0)
project(py_cpp LANGUAGES CXX)

add_subdirectory(pybind11)
pybind11_add_module(py_cpp py_cpp/core/src/add.cpp)