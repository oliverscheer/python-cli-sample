# MY CLI Tool

```bash
# import my external library

pip install ../../packages/mytoollibrary/dist/mytoollibrary-0.0.1-py3-none-any.whl -t external_packages/mytoollibrary

```

## Local running

```bash
python -m cli.main
```

Lorem Ipsum

## Install as cli app

[Source](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/)


```bash
pip install build
python -m build

pip install dist/mycliapp-0.0.1-py3-none-any.whl --force-reinstall

```


testing clean env

```bash
# create env
python -m venv .env/fresh-install-test

# activate env
. .env/fresh-install-test/bin/activate

pip install dist/mycliapp-0.0.1-py3-none-any.whl

ls .env/fresh-install-test/bin/
my-cli-app
my-other-cli-app
```


## latest version
```bash
python -m venv .env/create-cli-package
. .env/create-cli-package/bin/activate
cp ../../packages/mytoollibrary/dist/mytoollibrary-0.0.1-py3-none-any.whl .
pip install mytoollibrary-0.0.1-py3-none-any.whl --force-reinstall

pip install ../../packages/mytoollibrary/dist/mytoollibrary-0.0.1-py3-none-any.whl -t external_packages/mytoollibrary


pip install build

python -m build
cd dist
pip install mycli-0.0.1-py3-none-any.whl --force-reinstall
tar -xzf mycli-0.0.1.tar.gz
cd ..

mycli --help
mycli text upper "Hello World!"
mycli text lower "Hello World!"


```