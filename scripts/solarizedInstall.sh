# set gnome-terminal, tmux, guake balckboard to solarized color scheme

sudo apt-get install dconf-cli

# set gnome-terminal solarized
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git ./third_party/gnome-terminal-colors-solarized
./third_party/gnome-terminal-colors-solarized/set_dark.sh

# set guake solarized
git clone https://github.com/coolwanglu/guake-colors-solarized.git ./third_party/guake-colors-solarized
./third_party/guake-colors-solarized/set_dark.sh solarized
