FROM registry.gitlab.com/musicscience37_ci/cpp-base-image-docker:v0-1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc-9=9.2.1-9ubuntu2 \
        g++-9=9.2.1-9ubuntu2 \
        libperlio-gzip-perl=0.19-1build4 \
        libjson-perl=4.02000-1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-9)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-9)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-9)" /usr/local/bin/gcov

WORKDIR /usr/local/lcov
RUN git clone https://github.com/linux-test-project/lcov.git && \
    cd lcov && \
    git checkout 40580cd65909bc8324ae09b36bca2e178652ff3f && \
    make install && \
    cd .. && \
    rm -r lcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
