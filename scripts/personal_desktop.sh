display=(unity-tweak-tool wallch guake)


install_lists=(
${display[@]}
)

# Begin to apt get install
for name in ${install_lists[@]}; do
  $1 install $name
done
