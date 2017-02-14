#!/usr/bin/env

import os

home_url = os.popen('echo $HOME').read().rstrip('\n')
setup_url = os.popen('pwd').read().rstrip('\n')


def clean_old_dotfiles(dotfile_list):
    home_list = os.listdir(home_url)
    for f in dotfile_list:
        if f in home_list:
            os.remove(home_url + '/' + f)
            print ('Clean the old file :' + f)


def ln_new_dotfiles(dotfile_list):
    for f in dotfile_list:
        os.system(
            'ln -s {0}/dotfiles/{1} {2}/{1}'.format(setup_url, f, home_url))


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

if __name__ == '__main__':
    initialize()
