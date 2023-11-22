<h1 align="center">
  FOND 4 LTL<sub>f</sub>
</h1>

<p align="center">
  <a href="https://pypi.org/project/FOND4LTLfPLTLf">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/ltlf2dfa" />
  </a>
  <a href="https://github.com/whitemech/FOND4LTLfPLTLf/blob/master/LICENSE">
    <img alt="GitHub" src="https://img.shields.io/badge/license-LGPLv3%2B-blue">
  </a>
</p>
<p align="center">
  <a href="">
    <img alt="test" src="https://github.com/whitemech/FOND4LTLfPLTLf/workflows/test/badge.svg">
  </a>
  <a href="">
    <img alt="lint" src="https://github.com/whitemech/FOND4LTLfPLTLf/workflows/lint/badge.svg">
  </a>
  <a href="">
    <img alt="docs" src="https://github.com/whitemech/FOND4LTLfPLTLf/workflows/docs/badge.svg">
  </a>
  <a href="https://codecov.io/gh/whitemech/FOND4LTLfPLTLf">
    <img src="https://codecov.io/gh/whitemech/FOND4LTLfPLTLf/branch/master/graph/badge.svg?token=KKWRAH29O7"/>
  </a>
</p>
<p align="center">
  <a href="https://img.shields.io/badge/flake8-checked-blueviolet">
    <img alt="" src="https://img.shields.io/badge/flake8-checked-blueviolet">
  </a>
  <a href="https://img.shields.io/badge/mypy-checked-blue">
    <img alt="" src="https://img.shields.io/badge/mypy-checked-blue">
  </a>
  <a href="https://img.shields.io/badge/isort-checked-yellow">
    <img alt="isort" src="https://img.shields.io/badge/isort-checked-yellow" />
  </a>
  <a href="https://img.shields.io/badge/code%20style-black-black">
    <img alt="black" src="https://img.shields.io/badge/code%20style-black-black" />
  </a>
  <a href="https://www.mkdocs.org/">
    <img alt="" src="https://img.shields.io/badge/docs-mkdocs-9cf">
</p>
<p align="center">
<a href="https://doi.org/10.5281/zenodo.4876281"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4876281.svg" alt="DOI"></a>
</p>

FOND 4 LTL<sub>f</sub> is a tool that compiles Fully Observable Non-Deterministic (FOND) planning
problems with temporally extended goals, specified either in LTL<sub>f</sub> or in PLTL<sub>f</sub>, into classical FOND
planning problems.

It is also available online at [https://fond4ltlf.herokuapp.com/](https://fond4ltlf.herokuapp.com/).

## Prerequisites

This tool is based on the following libraries:

- [ltlf2dfa 1.0.1](https://pypi.org/project/ltlf2dfa/)
- [ply](https://pypi.org/project/ply/)
- [click](https://pypi.org/project/click/)

They are automatically added while installing FOND4LTL<sub>f</sub>.

## Install

- Intall from source (`master` branch):

```
pip install git+https://github.com/whitemech/FOND4LTLf.git
```

- or, clone the repository and install:

```
git clone https://github.com/whitemech/FOND4LTLf.git
cd fond4ltlfpltlf
pip install .
```

### Docker Instructions- Creating an Image and Spinning a Container

Make sure you have Docker installed. If not, follow the instructions [here](https://docs.docker.com/engine/install).

### Docker Commands to build the image

1. `cd` into the root of the project

2. Build the image from the Dockerfile

```bash
docker build -t <image_name> .
```

Note: the dot looks for a Dockerfile in the current repository. Then spin an instance of the container by using the following command

```bash
docker run -it --name <docker_container_name> <docker_image_name>
```

For volume binding

```bash
docker run -v <HOST-PATH>:<Container-path>
```

For example, to volume bind your local directory to the `FOND4LTLf` folder inside the Docker, use the following command

```bash
docker run -it -v $PWD:/FOND4LTLf --name <docker_container_name> <dokcer_image_name>
```

Here `<docker_container_name>` is any name of your choice and `<image_name>` is the docker image name from above. `-it` and `-v` are flags to run an interactive terminal and volume bind respectively. 

Additionally, if you are more used to GUI and would like to edit or attach a container instance to VSCode ([Link](https://code.visualstudio.com/docs/devcontainers/containers)) then follow the instructions below:

#### Attaching the remote container to VScode


1. Make sure you have the right VS code extensions installed
   * install docker extension
   * install python extension
   * install remote container extension
   * Now click on the `Remote Explore` tab on the left and attach VScode to a container.
2. This will launch a new vs code attached to the container and prompt you to a location to attach to. The default is root, and you can just press enter. Congrats, you have attached your container to VSCode.


## How To Use

Use the command line interface:

```bash
fond4ltlfpltlf -d <path/to/domain.pddl> -p <path/to/problem.pddl> -g "formula"
```

You can also specify custom output paths for the new domain and the new problem using `--out-domain` or `-outd`
and `--out-problem` or `-outp`.

## Features

* Syntax and parsing support FOND Planning in PDDL
* Compilation of Deterministic Finite-state Automaton into PDDL

## Tests

To run tests: `tox`

To run only the code tests: `tox -e py3.8`

To run only the code style checks: `tox -e flake8`

### Note on Tox

If you are installing `tox` using gloabl Python interperter within the Dockerfile then use the following commands:

To run tests: `python3 -m tox`

To run only the code tests: `python3 -m tox -e py3.8`

To run only the code style checks: `python3 -m tox -e flake8`


## License

FOND4LTL<sub>f</sub> is released under the GNU Lesser General Public License v3.0 or later (LGPLv3+).

Copyright 2019-2022 WhiteMech

## Author

[Francesco Fuggitti](https://francescofuggitti.github.io/)


