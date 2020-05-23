FROM registry.gitlab.com/musicscience37_ci/cpp-base-image-docker:v2-0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc-7=7.5.0-6ubuntu2 \
        g++-7=7.5.0-6ubuntu2 \
        lcov=1.14-2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-7)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-7)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-7)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
