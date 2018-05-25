#!/usr/bin/env python

import sys
import os
from setters import utils
from setters import vimsetter
from setters import tmuxsetter

home_url = os.path.expanduser('~')
setup_url = os.getcwd()


def clean_old_dotfiles(dotfile_list):
    for f in dotfile_list:
        check_url = os.path.join(home_url, f)
        utils.check_and_clean_old_link(check_url)


def ln_new_dotfiles(dotfile_list):
    for f in dotfile_list:
        src = os.path.join(setup_url, 'dotfiles', f)
        dst = os.path.join(home_url, f)
        try:
            os.symlink(src, dst)
        except:
            print("link %s failed!" % f)


def clean_gitrepos_config():
    os.system("rm -rf ./vim/bundle ./vim/tempfiles ./tmux/plugins")
    os.system("rm -rf ./third_party/*")


def new_try():
    # add new commands below
    # when it is tested ok, move it to the personalize
    pass


if __name__ == '__main__':

    l = len(sys.argv)
    if l == 2:
        if sys.argv[1] == 'clean':
            clean_gitrepos_config()
    elif (l == 1):
        # vim and tmux is the must install file
        utils.bash_config(setup_url, 'basicInstall.sh')
        print("Config the vim and tmux...")
        vimsetter.config(setup_url, home_url)
        tmuxsetter.config(setup_url, home_url)

        print("Begin to ln the dotfiles...")
        dotfile_list = os.listdir('./dotfiles')
        dotfile_list.remove('.zshrc')
        clean_old_dotfiles(dotfile_list)
        ln_new_dotfiles(dotfile_list)

        utils.bash_config(setup_url, 'setupGit.sh')

        print("Complete basic init. It is alternative installation:")

        print('If you want to install zsh and use your default dotfile? [y/n]')
        ch = raw_input()
        if (ch == 'y'):
            utils.bash_config(setup_url, 'zshinstall.sh')

        print('If you want to install personal Desktop utils? [y/n]')
        ch = raw_input()
        if (ch == 'y'):
            utils.bash_config(setup_url, 'personal_desktop.sh')

        print("If you want to install some good ubuntu-icons? [y/n]")
        ch = raw_input()
        if (ch == 'y'):
            utils.bash_config(setup_url, 'iconsInstall.sh')

        print(
            "If you want to install Solarized color scheme for the terminal? [y/n]")
        ch = raw_input()
        if (ch == 'y'):
            utils.bash_config(setup_url, 'solarizedInstall.sh')

        print("If you want to install node6x? [y/n]")
        ch = raw_input()
        if (ch == 'y'):
            utils.bash_config(setup_url, 'nodejs6Xinstall.sh')

        print("Do you want to delete the sample wallpapers? (y/n) (Default is n)")
        ch = raw_input()
        if ch == 'y':
            utils.clean_wallpaper(setup_url)
