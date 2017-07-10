# set gnome-terminal, tmux, guake balckboard to solarized color scheme

sudo $1 install dconf-cli

# set gnome-terminal solarized
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git ./third_party/gnome-terminal-colors-solarized
./third_party/gnome-terminal-colors-solarized/set_dark.sh

if [ -f ./dircolors ]; then
    echo "Use the dircolor!"
    eval `dircolors ./dircolors`
fi

source .bashrc
