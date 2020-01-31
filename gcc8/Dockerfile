FROM registry.gitlab.com/musicscience37_ci/cpp-base-image-docker:v0-1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc-8=8.3.0-23ubuntu2 \
        g++-8=8.3.0-23ubuntu2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-8)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-8)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-8)" /usr/local/bin/gcov

WORKDIR /usr/local/lcov
RUN wget -nv https://github.com/linux-test-project/lcov/releases/download/v1.14/lcov-1.14.tar.gz && \
    tar xf lcov-1.14.tar.gz && \
    make -C lcov-1.14 install && \
    rm -r lcov-1.14 lcov-1.14.tar.gz

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
