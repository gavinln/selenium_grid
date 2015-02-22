#!/bin/bash
# Strict mode
set -euo pipefail

# run ipython using python 2.x
python /usr/local/bin/ipython notebook --no-browser --port 8888 --ip=0.0.0.0 --notebook-dir=/notebook-dir
#/opt/anaconda/bin/ipython notebook --no-browser --port 8888 --ip=0.0.0.0 --notebook-dir=/notebook-dir
