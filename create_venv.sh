#!/bin/bash

set -e # exit on error

ENV_NAME="cnn-env"

python -m venv $ENV_NAME

source $ENV_NAME/bin/activate

pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

