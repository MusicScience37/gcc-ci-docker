ARG UBUNTU_VERSION
FROM registry.gitlab.com/musicscience37projects/docker/cpp-base-image-docker:${UBUNTU_VERSION}

ARG GCC_VERSION
RUN apt-get update && \
    apt-get install -y \
    gcc-${GCC_VERSION} \
    g++-${GCC_VERSION} \
    lcov && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/gcc  gcc  "$(command -v gcc-${GCC_VERSION})"  10000 && \
    update-alternatives --install /usr/bin/g++  g++  "$(command -v g++-${GCC_VERSION})"  10000 && \
    update-alternatives --install /usr/bin/gcov gcov "$(command -v gcov-${GCC_VERSION})" 10000

ENV CC=/usr/bin/gcc
ENV CXX=/usr/bin/g++

WORKDIR /root
