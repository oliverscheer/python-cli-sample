#!/bin/bash

ROOT_FOLDER="/workspaces/python-cli-sample"

echo "Build Packages First"

cd packages/mytoollibrary
./build.sh

cd $ROOT_FOLDER

echo "Build CLI apps"

cd cli-apps/mycli
./build.sh