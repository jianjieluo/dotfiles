import os
import utils


def config_tempfiles(vimconfig_dir):
    tempfiles = ['.undo', '.swp', '.backup']
    tempfiles_url = os.path.join(vimconfig_dir, 'tempfiles')
    if not os.path.exists(tempfiles_url):
        os.makedirs(tempfiles_url)
    for each in tempfiles:
        f_url = os.path.join(tempfiles_url, each)
        if not os.path.exists(f_url):
            os.makedirs(f_url)


def config(setup_url, home_url):
    src = os.path.join(setup_url, 'vim')
    dst = os.path.join(home_url, '.vim')

    utils.check_and_clean_old_link(dst)
    os.symlink(src, dst)

    plugin_url = os.path.join(dst, 'bundle')
    init_vundle_cmd = "git clone https://github.com/VundleVim/Vundle.vim.git {0}/Vundle.vim".format(
        plugin_url)
    os.system(init_vundle_cmd)
    config_tempfiles(dst)
