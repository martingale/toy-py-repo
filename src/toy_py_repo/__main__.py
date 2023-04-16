"""Entry-point module, in case of using `python -m toy_py_repo`."""

import typer

from toy_py_repo.cli import main

typer.run(main)
