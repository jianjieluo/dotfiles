sudo apt-get install zsh 


# check for oh-my-zsh config
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  echo "Installing oh-my-zsh framework..."
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
else
  echo "Already exists oh-my-zsh"
fi