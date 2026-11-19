# Lab 7 Fuzz Testing

This lab uses Hypothesis to fuzz the sender domain, first link, and uppercase ratio functions. The fixed functions return safe empty values for invalid input, and the final suite checks both fuzzed input and expected behavior.

## Install and run

From this directory:

```sh
python -m pip install -r requirements.txt
```

Run the original interactive program with ordinary inputs:

```sh
python baseline_spam_scoring.py
```

Use these sample inputs when prompted:

```text
offers@Deals.com
Visit https://example.com now
FREE prize NOW
```

The original implementation is kept as `baseline_spam_scoring.py` so the fuzz failures can be reproduced. Run the intentionally failing discovery tests with:

```sh
python -m pytest -q --tb=no fuzz_failure_demo.py
```

The three tests expose failures for invalid sender input, text without a link, and text without letters. The demo file is not collected by the normal test command.

Run the fixed interactive program with the same sample inputs:

```sh
python spam_scoring.py
```

Run the passing Hypothesis and regression tests:

```sh
python -m pytest -q test_spam_scoring.py
```

## Screenshots for the report

1. Original program output from `python baseline_spam_scoring.py`.
2. Failing fuzz test output from `python -m pytest -q fuzz_failure_demo.py`.
3. Fixed program output from `python spam_scoring.py`.
4. Passing test output from `python -m pytest -q test_spam_scoring.py`.

## Report

The completed screenshot report is [PES2UG24CS098_SE_Lab_7.pdf](PES2UG24CS098_SE_Lab_7.pdf). The editable Pages evidence file is `Lab_7_FuzzTesting_Evidence.pages`.
