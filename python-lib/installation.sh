#!/bin/bash

# exit on failure
set -e

# ensure is root
if [ $(id -u) -ne 0 ]; then
    echo 'You must be root to run this command.'
    exit 1
fi

# constants
SRC=lib-jtools/
DEST_PATH=/usr/lib/python3/dist-packages/jtools/

#-- functions ------------------------------------------------#

help_info () {
    echo "About: Handle python library global installation"
    echo "Usage:"
    echo "    $0 ACTION"
    echo "    where ACTION = install | uninstall"
    echo ""
}

install () {
    if [ ! -d "$SRC" ]; then
        echo "Cannot find the directory $SRC in cwd"
        exit 1
    else
        echo "Installing..."
        rsync -av --mkpath $SRC $DEST_PATH
        chown -R root:root $DEST_PATH
        echo "...Finished"
    fi
}

uninstall () {
    read -p "Confirm uninstallation? (y/n): " YN
    if [[ "$YN" != "y" ]] ; then
        echo "Canceled"
    else
        echo "Uninstalling..."
        rm -rf $DEST_PATH
        echo "...Finshed"
    fi
}

#-- main ------------------------------------------------#

ACTION=$1
if [[ "$ACTION" == "install" ]] ; then
    install
elif [[ "$ACTION" == "uninstall" ]] ; then
    uninstall
else
    help_info
fi

