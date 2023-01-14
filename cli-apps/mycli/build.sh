#!/bin/bash
rm -rf dist mycli.egg-info

pip install build
python -m build
pip install dist/mycli-0.0.1-py3-none-any.whl --force-reinstall

cd dist
tar -xzf dist/mycli-0.0.1.tar.gz
cd ..

mycli --help