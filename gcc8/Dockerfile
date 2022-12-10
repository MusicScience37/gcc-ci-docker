FROM registry.gitlab.com/musicscience37projects/docker/cpp-base-image-docker:focal

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc-8 \
    g++-8 \
    lcov && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-8)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-8)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-8)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
