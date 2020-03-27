# gcc-ci-docker

[![dockeri.co](https://dockeri.co/image/musicscience37/gcc-ci)](https://hub.docker.com/r/musicscience37/gcc-ci)

![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/musicscience37/gcc-ci)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/musicscience37/gcc-ci)

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/MusicScience37/gcc-ci-docker?label=latest)

[![pipeline status](https://gitlab.com/musicscience37_ci/gcc-ci-docker/badges/develop/pipeline.svg)](https://gitlab.com/musicscience37_ci/gcc-ci-docker/commits/develop)

Docker container image for CI of C/C++ with GCC.

Container images contains the following tools:

- gcc, g++, gcov, lcov
- make, cmake
- curl, wget
- git
- python3
- perl

The version of GCC is as following:

| Tag of Container | Version of GCC |
| :--------------- | :------------- |
| gcc7             | 7.5.0          |
| gcc8 (latest)    | 8.3.0          |
| gcc9             | 9.2.1          |

The container image with tag `gcc9` uses unstable version of lcov
because the latest stable version of lcov doesn't support
GCC version 9.
So the container image with tag `gcc9` is less stable than
one with tag `gcc8`.

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37_ci/gcc-ci-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37_ci/gcc-ci-docker:gcc8`
- [Docker Hub](https://hub.docker.com/r/musicscience37/gcc-ci)
  - latest stable image: `docker pull musicscience37/gcc-ci`

## Repositories

- [GitLab](https://gitlab.com/musicscience37_ci/gcc-ci-docker):
  for development including CI
- [Github](https://github.com/MusicScience37/gcc-ci-docker):
  mirror repository for use in Docker Hub

## Test

To run a test of this project, execute the `run_test.sh` script.
It requires docker and docker-compose commands installed.
