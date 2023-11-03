# Python Project Template

A starter template for AI Hero course takers.

## Setup
1. Note down what your current Python version is with `python --version` (e.g. `3.9.1``)
2. In `pyproject.toml` change the value of `tool.black.target_version` to whatever is your current `major.minor` version (e.g. `py39`)
3. In `.pre-commit-config.yaml` change the value of `python3.9` to whatever is is your current `major.minor` version (e.g. `python3.9`)
4. Run this on your console:

```sh
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pre-commit install
pre-commit autoupdate
```
