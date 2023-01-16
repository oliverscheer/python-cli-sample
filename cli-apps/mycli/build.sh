#!/bin/bash
rm -rf dist mycli.egg-info

pip install \
    ../../packages/mytoollibrary/dist/mytoollibrary-0.0.1-py3-none-any.whl \
    -t external-packages/mytoollibrary


pip install build
python -m build

# Debug help: Unzip dist package for checks
cd dist
tar -xzf mycli-0.0.1.tar.gz
cd ..

# Install my CLI application
pip install dist/mycli-0.0.1-py3-none-any.whl --force-reinstall


# mycli --help

# # Internal tests
# mycli text upper "Hello World!"
# mycli text lower "Hello World!"

# # Calling referenced package functions
# mycli circle area -r 3.0