import os
import shutil
from config import install_tool


def check_and_clean_old_link(url):
    if os.path.islink(url):
        os.unlink(url)
    else:
        if os.path.exists(url):
            if os.path.isdir(url):
                shutil.rmtree(url)
            else:
                os.remove(url)


def bash_config(setup_url, name):
    os.system('bash {0}/scripts/{1} {2}'.format(setup_url, name, install_tool))
