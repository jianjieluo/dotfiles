# Install personal utils, change the config lists if necessary

# classified apt-get config lists
utils=(tree locate pip mysql-server mysql-client)
# codings=(clang clang-format pip)

install_lists=(
${utils[@]}
# ${codings[@]}
)

# Begin to apt get install
for name in ${install_lists[@]}; do
  $1 install $name
done
