FROM registry.gitlab.com/musicscience37/cpp-base-image-docker:focal-v5-0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc-9=9.4.0-1ubuntu1~20.04.1 \
    g++-9=9.4.0-1ubuntu1~20.04.1 \
    lcov=1.14-2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-9)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-9)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-9)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
