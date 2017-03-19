#!/usr/bin/env bash

command_exists () {
    type "$1" &> /dev/null ;
}

# If we have a virtual env active then deactivate
if command_exists deactivate
then
    deactivate
fi

# Simple setup script to install temporary venv into project directory to make cleaning up easier
if [ ! -d ./venv ]
then
    sudo easy_install pip3
    pip3 install virtualenv
    virtualenv venv
    source ./venv/bin/activate
    # fabric so we can use fab commands
    pip3 install -r requirements.txt
fi

source ./venv/bin/activate
