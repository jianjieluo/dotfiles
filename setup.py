# python file
#================================================
#      Filename: setup.py
#
#        Author: longj - luojj26@gmail.com
#   Description: ---
#   Head Create: 2017-02-16 22:05:33
# Last Modified: 2017-02-16 22:11:13
#================================================

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
            print "link %s failed!" % f


def server_setup():
    print "Check for basic softwares..."
    utils.bash_config(setup_url, 'basicInstall.sh')

    print "Try to config git..."
    utils.bash_config(setup_url, 'setupGit.sh')

    print "Config the vim and tmux..."
    vimsetter.config(setup_url, home_url)
    tmuxsetter.config(setup_url, home_url)

    print "Begin to ln the dotfiles..."
    dotfile_list = os.listdir('./dotfiles')
    clean_old_dotfiles(dotfile_list)
    ln_new_dotfiles(dotfile_list)

    print "Update global .gitconfig..."
    utils.bash_config(setup_url, 'setupGit.sh')

    print "Begin to install nodejs 6.x ..."
    utils.bash_config(setup_url, 'nodejs6Xinstall.sh')


def personal_desktop_setup():

    print "Begin to install personal utils from apt..."
    utils.bash_config(setup_url, 'personalInstall.sh')

    print "Begin to download some good ubuntu-icons..."
    utils.bash_config(setup_url, 'iconsInstall.sh')

    print "Begin to set Solarized color scheme for the working environment..."
    utils.bash_config(setup_url, 'solarizedInstall.sh')


def clean_gitrepos_config():
    os.system("rm -rf ./vim/bundle ./vim/tempfiles ./tmux/plugins")
    os.system("rm -rf ./third_party")


def new_try():
    # add new commands below
    # when it is tested ok, move it to the personalize
    pass

if __name__ == '__main__':
    l = len(sys.argv)
    if l == 2:
        if sys.argv[1] == 'clean':
            clean_gitrepos_config()
        elif sys.argv[1] == 'dev':
            new_try()
        elif sys.argv[1] == 'server':
            server_setup()
            utils.clean_wallpaper(setup_url)
        elif sys.argv[1] == 'desktop':
            server_setup()

            print "Do you want to delete the sample wallpapers? (yes/no) (Default is no)"
            choice = raw_input()
            if choice == 'yes':
                utils.clean_wallpaper(setup_url)

            print "Do you want to execute the personal setting? (yes/no) (Default is no)"
            choice = raw_input()
            if choice == 'yes':
                personal_desktop_setup()
                print "Personalized Done!!"
            else:
                print "initialization Process Finished !"
        else:
            print "Invalid argv."
            print "Options: \'clean\', \'dev\', 'server', 'desktop'"
            print "Run it again, please :)"
    elif l > 2:
        print "Too much commands argv!"
    elif l == 1:
        print "You should add an argv."
        print "Invalid argv."
        print "Options: \'clean\', \'dev\', 'server', 'desktop'"
        print "Run it again, please :)"
