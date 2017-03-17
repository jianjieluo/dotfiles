#!/usr/bin/env bash

software_leak_filling() {
  if [ ! -x "/usr/bin/$1" ] ; then
    echo "Installing $1..."
    $2 install $1
  else
    # echo "$2 Installing $1..."
    echo "System has already haven $1"
  fi
}

terminal_get_list=(git vim tmux zsh curl)

for name in ${terminal_get_list[@]}; do
  software_leak_filling $name $1
done


# check for oh-my-zsh config
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  echo "Installing oh-my-zsh framework..."
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
else
  echo "Already exists oh-my-zsh"
fi
