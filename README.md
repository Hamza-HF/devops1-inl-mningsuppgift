# Unit Converter

A Python unit converter built as part of a DevOps course assignment.
Demonstrates version control with Git, automated testing with pytest,
and a CI pipeline using GitHub Actions.

## What it does

Converts between common units across three categories:

- **Temperature** — Celsius, Fahrenheit, Kelvin
- **Distance** — km/miles, meters/feet
- **Weight** — kg/lbs, grams/ounces

Each category lives in its own module under `converters/`.

## Project structure

```
unit-converter/
├── .github/
│   └── workflows/
│       └── ci.yml
├── converters/
│   ├── __init__.py
│   ├── temperature.py
│   ├── distance.py
│   └── weight.py
├── tests/
│   ├── test_temperature.py
│   ├── test_distance.py
│   └── test_weight.py
├── main.py
├── requirements.txt
└── README.md
```

## How to run locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the converter:

```
python main.py
```

Run the tests:

```
pytest tests/ -v
```

## How the CI pipeline works

Defined in `.github/workflows/ci.yml`, triggers automatically on every push to `main`.

Steps:
1. **Checkout** — downloads the repo onto the GitHub Actions runner
2. **Set up Python 3.12** — installs the correct Python version
3. **Install dependencies** — runs `pip install -r requirements.txt`
4. **Lint with flake8** — checks the code for style and syntax issues
5. **Run tests** — runs all tests in `tests/` using `pytest -v`

If any test fails the pipeline fails and the commit is marked as broken.