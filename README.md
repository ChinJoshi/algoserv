run locally with `uv run fastapi dev`
run prod with `uv run fastapi run`

to deploy:

1. bundle deps
   uv export --frozen --no-dev --no-editable -o requirements.txt
   uv pip install \
    --no-installer-metadata \
    --no-compile-bytecode \
    --python-platform x86_64-manylinux2014 \
    --python 3.13 \
    --target lambda \
    -r requirements.txt

2. then copy the app dir into the lambda dir

3. then run `cdk deploy` to deploy
