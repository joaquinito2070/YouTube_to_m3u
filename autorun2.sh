#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

python3 scripts/generator.py
