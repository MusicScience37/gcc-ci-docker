ARG UBUNTU_VERSION
FROM registry.gitlab.com/musicscience37projects/docker/cpp-base-image-docker:${UBUNTU_VERSION}

ARG GCC_VERSION
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc-${GCC_VERSION} \
    g++-${GCC_VERSION} \
    lcov && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-${GCC_VERSION})" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-${GCC_VERSION})" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-${GCC_VERSION})" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
