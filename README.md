<div align="center">

<!-- Provide information on your repository here. -->

<!-- <img src=./style/repo.png width="800"> -->

&nbsp;

![Tests](https://github.com/martingale/toy-py-repo/actions/workflows/tests.yml/badge.svg)
![Quality](https://github.com/martingale/toy-py-repo/actions/workflows/quality.yml/badge.svg)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

# User Guide

## Requirements

- Python >= 3.10
- OS: Ubuntu, MacOS, Windows

## Installation

Pip installing the package from PyPI is not yet available. Instead, download [from this link](https://github.com/martingale/toy-py-repo/archive/refs/heads/main.zip) and unzip. You will also need to change the folder name from toy-py-repo-main to toy-py-repo (or cd into toy-py-repo-main in step 2 below). Alternatively, if you have git installed, simply run 
```bash
git clone https://github.com/martingale/toy-py-repo
```
to install the package locally. After downloading, here are the steps to install the dependencies in a virtual environment using [PDM]:

1. `pip install pdm`
2. `cd toy-py-repo`
3. `pdm install`

## Usage

### Configuration

First edit the `./config/config.yaml` to your liking. Example config files can be found at `./config/`.

### Quick Start

After configuring the `./config/config.yaml`, simply run the following command in the project directory.
```bash
pdm run python -m toy_py_repo
```

### Detailed Usage
For a list of all the CLI arguments and options, run
```bash
pdm run python -m toy_py_repo --help
```

&nbsp;

# Developer Guide

## Setup

This project is [PDM]-managed, which is compatible with [PEP 582] and [PEP 621]. If you are a developer, first `pip install pdm` and then make your Python interpreter aware of [PEP 582]. If you are using bash, you can do this by running

```bash
pdm --pep582 >> ~/.bash_profile
```

Similarly, for zsh run

```bash
pdm --pep582 >> ~/.zshrc
```
Then `git clone` the project and `mkdir __pypackages__` in the project directory. This lets [PDM] know that you are using [PEP 582] instead of virtualenv. Now you can `pdm install`, which will install all the dependencies in the project directory.

## Development

### IDE Support

In order to configure your IDE to support [PEP 582], you can follow the instructions [here](https://pdm.fming.dev/latest/usage/pep582/).

### Pre-commit Hooks

The project also uses pre-commit hooks. Because the project uses [PDM], you **do not** need to `pip install pre-commit`. Instead, run directly
```bash
pdm run pre-commit install
```
in the project directory to install hooks to your local `.git`.

[pep 582]: https://www.python.org/dev/peps/pep-0582
[pep 621]: https://www.python.org/dev/peps/pep-0621
[PDM]: https://pdm.fming.dev
