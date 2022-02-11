FROM registry.gitlab.com/musicscience37_ci/cpp-base-image-docker:jammy-v4-1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc-11=11.2.0-16ubuntu1 \
    g++-11=11.2.0-16ubuntu1 \
    lcov=1.15-1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-11)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-11)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-11)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
