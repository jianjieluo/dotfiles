#!/usr/bin/env bash

software_leak_filling() {
  # cd $HOME
  if [ ! -x "/usr/bin/$1" ] ; then
    echo "Installing $1..."
    # apt-get install $1
  else
    echo "System has already haven $1"
  fi
}

terminal_get_list=(git vim tmux zsh curl clang cmake tree ssh openssh-server)

for name in ${terminal_get_list[@]}; do
  software_leak_filling $name
done

if [ ! -d "$HOME/.oh-my-zsh" ]; then
  echo "Installing oh-my-zsh framework..."
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
else
  echo "Already exists oh-my-zsh"
fi
