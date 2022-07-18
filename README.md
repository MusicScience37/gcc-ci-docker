# gcc-ci-docker

[![dockeri.co](https://dockeri.co/image/musicscience37/gcc-ci)](https://hub.docker.com/r/musicscience37/gcc-ci)

[![pipeline status](https://gitlab.com/MusicScience37/gcc-ci-docker/badges/main/pipeline.svg)](https://gitlab.com/MusicScience37/gcc-ci-docker/-/commits/main)

Docker container image for CI of C/C++ with GCC.

Container images contains the following tools:

- gcc, g++, gcov, lcov
- make, cmake
- curl, wget
- git
- python3
- perl

The version of GCC is as following:

- gcc8
- gcc9
- gcc10
- gcc11
- gcc12

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37/gcc-ci-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37/gcc-ci-docker:gcc10`
- [Docker Hub](https://hub.docker.com/r/musicscience37/gcc-ci)
  - latest stable image: `musicscience37/gcc-ci`

## Repositories

- [GitLab](https://gitlab.com/musicscience37/gcc-ci-docker):
  for development including CI
- [Github](https://github.com/MusicScience37/gcc-ci-docker):
  mirror repository

## Testing

For test of this project,
use `./tool.py test` command.
