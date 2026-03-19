#!/bin/bash

python3 -m venv django_venv

source django_venv/bin/activate

pip install -r requirement.txt

echo "Virtual environment created and activated!"
