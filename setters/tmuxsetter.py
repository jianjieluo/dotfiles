import os
import utils


def config(setup_url, home_url):
    src = os.path.join(setup_url, 'tmux')
    dst = os.path.join(home_url, '.tmux')

    # construct soft link
    utils.check_and_clean_old_link(dst)
    os.symlink(src, dst)

    plugin_url = os.path.join(dst, 'plugins')
    init_tpm_cmd = "git clone https://github.com/tmux-plugins/tpm {0}/tpm".format(
        plugin_url)
    os.system(init_tpm_cmd)
