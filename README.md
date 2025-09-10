# GitHub Actions for Data Analysis — Practice Repo

This small repo demonstrates how to run data-analysis code and notebooks inside GitHub Actions.

Contents:
- `data/sample.csv` — tiny example dataset
- `notebooks/analysis.ipynb` — a Jupyter notebook that reads the CSV, does a tiny analysis and a plot
- `scripts/process.py` — helper functions used by the notebook and tested by pytest
- `tests/test_process.py` — pytest unit tests
- `.github/workflows/ci.yml` — CI: run tests and execute the notebook (papermill)
- `.github/workflows/lint.yml` — code style and lint check
- `.github/workflows/self-hosted-example.yml` — example dispatch job for self-hosted runners
