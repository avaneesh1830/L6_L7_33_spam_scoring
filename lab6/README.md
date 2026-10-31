# L6_L7_33 — Spam Scoring Filter

Lab 6: Code and Branch Coverage

## About

A small Python module that scores messages for spam signals, classifies them and summarises the state of an inbox.

## Files

| File | Description |
|------|-------------|
| `spam_scoring.py` | The module under test |
| `CodeCoverageTest_spam_scoring.py` | Tests for statement (line) coverage |
| `BranchCoverageTest_spam_scoring.py` | Additional tests for missed decision branches |
| `screenshots/` | Coverage report screenshots |

## Run the coverage stages

From this directory, run the statement coverage suite and report:

```sh
python -m coverage run -m pytest -q CodeCoverageTest_spam_scoring.py
python -m coverage report -m spam_scoring.py
```

Then run both suites with branch measurement:

```sh
python -m coverage run --branch -m pytest -q CodeCoverageTest_spam_scoring.py BranchCoverageTest_spam_scoring.py
python -m coverage report -m spam_scoring.py
```

The first report records statement coverage. The branch suite adds the missing outcome for a known sender whose score remains above zero.
