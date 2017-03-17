# Install personal utils, change the config lists if necessary

# classified apt-get config lists
utils=(tree locate guake)
codings=(clang clang-format pip)
display=(unity-tweak-tool wallch)

install_lists=(
${utils[@]}
${codings[@]}
${display[@]}
)

# Begin to apt get install
for name in ${install_lists[@]}; do
  $1 install $name
done
