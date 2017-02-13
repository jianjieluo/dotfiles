# set up git config
IFS=:
GIT=false
for d in $PATH
  do test -x $d/git && GIT=true
done
if $GIT
then
  echo "git found!"
  git config --global user.name "longjj"
  git config --global user.email "luojj26@mail2.sysu.edu.cn"
  git config --global core.excludesfile "$HOME/.gitignore"
else echo "no git"
fi
