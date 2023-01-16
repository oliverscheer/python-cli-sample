#!/bin/bash
set -e

ROOT_FOLDER="/workspaces/python-cli-sample"

echo "Run tests for packages"
cd "$ROOT_FOLDER/packages/mytoollibrary"
pytest .

echo "Build Packages First"
cd "$ROOT_FOLDER/packages/mytoollibrary"

pip install build
python -m build

pip install \
    "$ROOT_FOLDER/packages/mytoollibrary/dist/mytoollibrary-0.0.1-py3-none-any.whl" \
    -t "$ROOT_FOLDER/cli-apps/mycli/external_packages/mytoollibrary"


echo "Run tests for CLI app"
cd "$ROOT_FOLDER/cli-apps/mycli"
pytest .

echo "Build CLI apps"
cd "$ROOT_FOLDER/cli-apps/mycli"

pip install build
python -m build

# # Debug help: Unzip dist package for checks
# cd dist
# tar -xzf mycli-0.0.1.tar.gz
# cd ..

# Install my CLI application
pip install dist/mycli-0.0.1-py3-none-any.whl --force-reinstall


cd "$ROOT_FOLDER"

echo "Some tests"

# Internal tests
mycli --help

mycli text upper "Hello World!"
mycli text lower "Hello World!"

# Calling referenced package functions
mycli circle area -r 3.0