display=(unity-tweak-tool)


install_lists=(
${display[@]}
)

# Begin to apt get install
for name in ${install_lists[@]}; do
  sudo $1 install $name
done
