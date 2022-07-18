FROM registry.gitlab.com/musicscience37/cpp-base-image-docker:jammy

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc-11 \
    g++-11 \
    lcov && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-11)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-11)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-11)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
