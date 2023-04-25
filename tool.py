#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2022 Kenta Kabashima
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""Tool to create and test Docker image.
"""

import datetime
import dataclasses
import os
import subprocess

import click

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

GITLAB_IMAGE_URL = "registry.gitlab.com/musicscience37projects/docker/gcc-ci-docker"
DOCKER_HUB_IMAGE_URL = "musicscience37/gcc-ci"


@dataclasses.dataclass
class Image:
    tag: str
    ubuntu_version: str
    gcc_version: int


def create_image(gcc_version: int, ubuntu_version: str) -> Image:
    return Image(
        tag=f"gcc{gcc_version}",
        ubuntu_version=ubuntu_version,
        gcc_version=gcc_version,
    )


IMAGE_LIST = [
    create_image(gcc_version=8, ubuntu_version="focal"),
    create_image(gcc_version=9, ubuntu_version="jammy"),
    create_image(gcc_version=10, ubuntu_version="jammy"),
    create_image(gcc_version=11, ubuntu_version="jammy"),
    create_image(gcc_version=12, ubuntu_version="kinetic"),
    create_image(gcc_version=13, ubuntu_version="lunar"),
]

IMAGE_MAP = {image.tag: image for image in IMAGE_LIST}


IMAGE_TAGS = [image.tag for image in IMAGE_LIST]
LATEST_IMAGE_TAG = "gcc11"


@click.group()
def cli():
    pass


def _run_command(command: list[str]):
    """Run a command.

    Args:
        command (list[str]): Command.
    """

    click.secho(f"> {command}", bold=True)
    subprocess.run(command, check=True, cwd=THIS_DIR)


def _create_time_stamp() -> str:
    """Create a time stamp.

    Returns:
        str: Time stamp.
    """

    return datetime.datetime.now().strftime("%Y%m%d")


def _build(image: Image, image_full_name: str):
    """Build Docker image.

    Args:
        image (Image): Information of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "build",
            "-t",
            image_full_name,
            "--build-arg",
            f"UBUNTU_VERSION={image.ubuntu_version}",
            "--build-arg",
            f"GCC_VERSION={image.gcc_version}",
            "gcc_in_ubuntu",
        ]
    )


def _test(image: Image, image_full_name: str):
    """Test Docker image.

    Args:
        image (Image): Information of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{THIS_DIR}/test:/home/test",
            image_full_name,
            "/home/test/run_test.sh",
            image.tag,
        ]
    )


def _tag_and_upload(image_full_name: str, another_image_full_name: str):
    _run_command(["docker", "tag", image_full_name, another_image_full_name])
    _run_command(["docker", "push", another_image_full_name])


def _upload(tag: str, image_full_name: str):
    """Upload Docker image.

    Args:
        tag (str): Tag of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "login",
            "-u",
            os.environ["CI_REGISTRY_USER"],
            "-p",
            os.environ["CI_REGISTRY_PASSWORD"],
            os.environ["CI_REGISTRY"],
        ]
    )
    _run_command(["docker", "push", image_full_name])
    _tag_and_upload(
        image_full_name=image_full_name,
        another_image_full_name=f"{GITLAB_IMAGE_URL}:{tag}-{_create_time_stamp()}",
    )
    if tag == LATEST_IMAGE_TAG:
        _tag_and_upload(
            image_full_name=image_full_name,
            another_image_full_name=f"{GITLAB_IMAGE_URL}:latest",
        )

    _run_command(
        [
            "docker",
            "login",
            "-u",
            os.environ["HUB_USER_NAME"],
            "-p",
            os.environ["HUB_ACCESS_TOKEN"],
        ]
    )
    _tag_and_upload(
        image_full_name=image_full_name,
        another_image_full_name=f"{DOCKER_HUB_IMAGE_URL}:{tag}",
    )
    if tag == LATEST_IMAGE_TAG:
        _tag_and_upload(
            image_full_name=image_full_name,
            another_image_full_name=f"{DOCKER_HUB_IMAGE_URL}:latest",
        )


@cli.command()
@click.argument("tag", type=click.Choice(IMAGE_TAGS))
def test(tag: str):
    """Build and test Docker image."""

    image = IMAGE_MAP[tag]
    image_full_name = f"{GITLAB_IMAGE_URL}:{tag}-test"
    _build(image=image, image_full_name=image_full_name)
    _test(image=image, image_full_name=image_full_name)


@cli.command()
@click.argument("tag", type=click.Choice(IMAGE_TAGS))
def update(tag: str):
    """Build, test, and update Docker image."""

    image = IMAGE_MAP[tag]
    image_full_name = f"{GITLAB_IMAGE_URL}:{tag}"
    _build(image=image, image_full_name=image_full_name)
    _test(image=image, image_full_name=image_full_name)
    _upload(tag=tag, image_full_name=image_full_name)


if __name__ == "__main__":
    cli()
