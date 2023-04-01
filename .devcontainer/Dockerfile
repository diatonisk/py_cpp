FROM ubuntu:22.04

WORKDIR /workspaces/py_cpp/

RUN apt update && \
    apt install python3-pip cmake gcc g++ -y && \
    pip3 install pybind11 autopep8