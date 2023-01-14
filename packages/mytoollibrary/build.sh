#!/bin/bash

rm -rf src/mytoollibrary.egg-info
rm -rf build
rm -rf dist

pip install build
python -m build

pip install dist/mytoollibrary-0.0.1-py3-none-any.whl --force-reinstall
