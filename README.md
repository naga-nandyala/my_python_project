# Sample Project with different formatting and linting tools

## initialize

```python
# create a virtual environment
python -m venv .venv
# activate the venv
source .venv/bin/activate
# to install default dependencies
pip install .
# to install development dependencies
pip install .[dev]
# to install npm dependencies(e.g markdownlint)
npm install -g markdownlint-cli
```

## contributor mode

```python
pip install -e [.dev]
pre-commit install
```

## some other commands

```unix
pre-commit clean
pre-commit autoupdate
```

## observations

- do we run these locally (vscode) ?
- import statements inside tests (using os.sys )
- no ruff, black, isort, notebook formatting, linting tools
- yamllint settings only in github actions. can we not centralize the config for both github and azdo
-
