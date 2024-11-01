# Sample Project with different formatting and linting tools

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
pip install .[dev]
```

## some other commands

```unix
pre-commit clean
pre-commit autoupdate
git commit -m "skip precommit" --no-verify
```
