#!/usr/bin/env bash

software_leak_filling() {
  if [ ! -x "/usr/bin/$1" ] ; then
    echo "Installing $1..."
    sudo $2 install $1
  else
    # echo "$2 Installing $1..."
    echo "System has already haven $1"
  fi
}

terminal_get_list=(git vim tmux curl)

for name in ${terminal_get_list[@]}; do
  software_leak_filling $name $1
done
