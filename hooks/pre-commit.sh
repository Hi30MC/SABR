#!/usr/bin/env bash

[[ -L "$PWD/.git/hooks/pre-commit" ]] || ln -vsf ../../hooks/pre-commit.sh "$PWD/.git/hooks/pre-commit"

# Your test commands here
set -e
pytest tests/unit/unit_tests.py -vs