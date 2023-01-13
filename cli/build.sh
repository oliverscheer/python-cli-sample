#!/bin/bash
rm -rf dist

pip install build
python -m build
pip install dist/mycliapp-0.0.1-py3-none-any.whl --force-reinstall

my-cli-app