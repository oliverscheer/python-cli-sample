# MY CLI Tool

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
