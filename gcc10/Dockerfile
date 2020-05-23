FROM registry.gitlab.com/musicscience37_ci/cpp-base-image-docker:v2-0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc-10=10-20200411-0ubuntu1 \
        g++-10=10-20200411-0ubuntu1 \
        lcov=1.14-2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    ln -s "$(command -v gcc-10)" /usr/local/bin/gcc && \
    ln -s "$(command -v g++-10)" /usr/local/bin/g++ && \
    ln -s "$(command -v gcov-10)" /usr/local/bin/gcov

ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++

WORKDIR /root
