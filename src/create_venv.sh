#!/usr/bin/env bash

VENVNAME=ADA

sudo apt update
sudo apt install -y python3-venv
sudo apt -y install zip unzip

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate

pip --version
pip install --upgrade pip
pip --version

# problems when installing from requirements.txt
#pip install ipython
#pip install jupyter
#python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install -r requirements.txt

deactivate
echo "build $VENVNAME"