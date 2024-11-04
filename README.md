# Sample Project with different formatting and linting tools--- dummy line

## initialize

```python
# create a virtual environment
python -m venv .venv
# activate the venv
source .venv/bin/activate
# to install default dependencies
pip install .
```

## contributor mode

```python
# to install development dependencies (contributor)
pip install --upgrade pip
pip install -e .[dev]
```

## some other commands

```unix
pre-commit install
pre-commit clean
pre-commit autoupdate
git commit -m "skip precommit" --no-verify
```
