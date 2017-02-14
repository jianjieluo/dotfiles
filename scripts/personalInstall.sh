# Install personal utils, change the config lists if necessary

# classified apt-get config lists
utils=(tree locate)
codings=(clang clang-format pip)
display=(unity-tweak-tool wallch)

apt_get_lists=(
${utils[@]}
${codings[@]}
${display[@]}
)

# Begin to apt get install
for name in ${apt_get_lists[@]}; do
  apt-get install $name
done
