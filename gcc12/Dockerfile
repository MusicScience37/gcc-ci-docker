FROM registry.gitlab.com/musicscience37/cpp-base-image-docker:jammy-v5-0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc-12=12-20220319-1ubuntu1 \
    g++-12=12-20220319-1ubuntu1 \
    lcov=1.15-1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-12)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-12)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-12)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
