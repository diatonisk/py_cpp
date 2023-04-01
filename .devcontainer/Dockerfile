FROM ubuntu:22.04

ENV WORKSPACE /workspaces/py_cpp

WORKDIR ${WORKSPACE}
RUN apt update && \
    apt install python3-pip python3-venv cmake gcc g++ -y && \
    pip3 install pybind11 autopep8 build ninja