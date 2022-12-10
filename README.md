# gcc-ci-docker

[![pipeline status](https://gitlab.com/MusicScience37Projects/docker/gcc-ci-docker/badges/main/pipeline.svg)](https://gitlab.com/MusicScience37Projects/docker/gcc-ci-docker/-/commits/main)
![Docker Pulls](https://img.shields.io/docker/pulls/musicscience37/gcc-ci)
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/musicscience37/gcc-ci/latest)

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

- [GitLab Container Registry](https://gitlab.com/MusicScience37Projects/docker/gcc-ci-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37projects/docker/gcc-ci-docker`
- [Docker Hub](https://hub.docker.com/r/musicscience37/gcc-ci)
  - latest stable image: `musicscience37/gcc-ci`

## Repositories

- [GitLab](https://gitlab.com/MusicScience37Projects/docker/gcc-ci-docker):
  for development including CI
- [Github](https://github.com/MusicScience37/gcc-ci-docker):
  mirror repository

## Testing

For test of this project,
use `./tool.py test` command.
