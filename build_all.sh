#!/bin/bash

ROOT_FOLDER="/workspaces/python-cli-sample"

echo "Run tests for packages"
cd "$ROOT_FOLDER/packages/mytoollibrary"
pytest .


echo "Run tests for CLI app"
cd "$ROOT_FOLDER/cli-apps/mycli"
pytest .


echo "Build Packages First"
cd "$ROOT_FOLDER/packages/mytoollibrary"
./build.sh


echo "Build CLI apps"
cd "$ROOT_FOLDER/cd cli-apps/mycli"
./build.sh

cd "$ROOT_FOLDER"
# Internal tests
mycli text upper "Hello World!"
mycli text lower "Hello World!"

# Calling referenced package functions
mycli circle area -r 3.0