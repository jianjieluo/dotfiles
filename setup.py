#!/usr/bin/env python

import os
import sys

home_url = os.path.expanduser('~')
setup_url = os.getcwd()


def clean_old_dotfiles(dotfile_list):
    for f in dotfile_list:
        check_url = os.path.join(home_url, f)
        if os.path.exists(check_url):
            os.remove(check_url)


def ln_new_dotfiles(dotfile_list):
    for f in dotfile_list:
        try:
            os.system(
                'ln -s {0}/dotfiles/{1} {2}/{1}'.format(setup_url, f, home_url))
        except:
            print "link %s failed!" % f


def config_vim_tempfiles(vimconfig_dir):
    tempfiles = ['.undo', '.swp', '.backup']
    tempfiles_url = os.path.join(vimconfig_dir, 'tempfiles')
    if not os.path.exists(tempfiles_url):
        os.makedirs(tempfiles_url)
    for each in tempfiles:
        f_url = os.path.join(tempfiles_url, each)
        if not os.path.exists(f_url):
            os.makedirs(f_url)


def config_terminal_utils(util_name):
    source = os.path.join(setup_url, util_name)
    target = os.path.join(home_url, '.' + util_name)

    # construct soft link
    if os.path.exists(target):
        os.unlink(target)
    os.symlink(source, target)

    # plugins initialization
    if util_name == "vim":
        plugin_url = os.path.join(target, 'bundle')
        init_vundle_cmd = "git clone https://github.com/VundleVim/Vundle.vim.git {0}/Vundle.vim".format(
            plugin_url)
        os.system(init_vundle_cmd)
        config_vim_tempfiles(target)
    elif util_name == 'tmux':
        plugin_url = os.path.join(target, 'plugins')
        init_tpm_cmd = "git clone https://github.com/tmux-plugins/tpm {0}/tpm".format(
            plugin_url)
        os.system(init_tpm_cmd)


def update_dotfiles_ln():
    print "Begin to ln the dotfiles..."
    dotfile_list = os.listdir('./dotfiles')
    clean_old_dotfiles(dotfile_list)
    ln_new_dotfiles(dotfile_list)


def initialize():
    print "Check for basic softwares..."
    os.system('sudo bash ./scripts/basicInstall.sh')

    print "Try to config git..."
    os.system('bash ./scripts/setupGit.sh')

    print "Config the vim and tmux..."
    config_terminal_utils('vim')
    config_terminal_utils('tmux')

    update_dotfiles_ln()

    print "Update global .gitconfig..."
    os.system('bash ./scripts/setupGit.sh')


def personalize():
    print "Begin to install nodejs 6.x ..."
    os.system('sudo bash ./scripts/nodejs6Xinstall.sh')

    print "Begin to install personal utils from apt..."
    os.system('sudo bash ./scripts/personalInstall.sh')

    print "Begin to download some good ubuntu-icons..."
    os.system('sudo bash ./scripts/iconsInstall.sh')

    print "Begin to set Solarized color scheme for the working environment..."
    os.system('bash ./scripts/solarizedInstall.sh')


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
        else:
            print "Invalid argv."
            print "Options: \'clean\', \'dev\' or no argv"
    elif l > 2:
        print "Too much commands argv!"
    elif l == 1:
        initialize()
        print "Do you want to execute the personal setting? (yes/no) (Default is no)"
        is_personalized = ''
        choice = raw_input()
        if choice == 'yes':
            personalize()
        else:
            pass
