# Dotfiles Auto Setting
`Johnny Law`  `SYSU in Guangdong Province, China`

## 0. Change log
### 2017.03.17
1. Now you can modify the `config.py` to choose other installing tools such as `yum` and `brew`, which imporves a litte capability, while there's a desktop icon config script used `apt update` to add repository key, leading to some exception.
2. Add clean Wallpapers option. You can delete the sample wallpapers if you don't like them.
3. Split some functions into several files, which are in `setters`
4. Supply `server` config and `desktop` config. You can custom your setting.

## 1. Overview
&ensp;&ensp;This repository contains my personal dotfiles and auto-setup tools through **python and bash** script. The master version is tested on **Ubuntu 16.04 LTS**. It may also work on other Debian or Ubuntu linux systems. When it goes to Mac, you may need to modify the `config.py` to use the correspoding tool.

&ensp;&ensp;It is welcomed to fork and change it for yourself. All you need to change is the personal setting config. Replacing some config with utils you prefer, then you can **use it to easily set up** a personalized environment when you move to a new machine or when you reinstall the system. ***I hope it can give all freshman an easy framework to start with***.

&ensp;&ensp;If you can fork it and update it for more compatible (such as mac), I will appreciate your help. **I will also continue to update it.**

---

## 2. Usage

### 1) Preparation

1. Install git, then execute this command in bash:`git clone https://github.com/longjj/dotfiles`
2. Modify the `config.py` to use your corresponding installing tool
2. Modify the `/scripts/setupGit.sh`,**<font size=5>set your own git global config</font>**. Then, if you want to totally use my config, you can **go to step (2) directly**.

#### The Overview of the Directories

1. If you don't want to use my dotfiles config, you need to replace the dotfiles in the directory `/dotfiles` with your own files. The `/dotfiles` contains all the config dotfiles being linked under `$HOME/`.
2. You can also change the `personalInstall.sh` to set your favouraite utils. All files in `/scripts` may be called in the `setup.py` so you can modify them to meet your need.
3. `/wallpaper` is just a directory to store several my favouraite commic heroes wallpapers as example. You can remove it if you don't like it.
4. `/vim` and `/tmux` are the directories that store **vim** and **tmux** plugins or useful custom setting files.
5. In `/vim`, there is a directory `/tempfiles` which contains three hidden directories `/.undo`, `/.swp` and `/.backup`. These directories collect all the temp files that vim create when you are using vim.
6. `/setters` is a python module which supports the `setup.py`

### 2) Eexecute Commands
```bash
cd dotfiles
sudo python setup.py [options]
```
#### Option List:
1. `clean`: clean the old plugins and temp files dir in the repository, which is handy for developing.
2. `dev`: If you want to add some new functions in the tool, you can put them in a block in `setup.py`, which will be helpful to your development.
**With no option, it will config some basic tools.**

#### Basic Tools List:
1. vim (use [vundle](https://github.com/VundleVim/Vundle.vim) to manage plugins)
2. zsh (use [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) framework)
3. tmux (use [tpm](https://github.com/tmux-plugins/tpm) to manage plugins)

**<font size=5>For deep uses and config, please check their official documents.</font>**

---

## 3. Notice

1. When config the icons, it is needed to add ppa to the system so you need to press enter to confirm timely, or it will be blocked.
2. Consider the similar blocking situation while installing other utils such as `mysql-server`.

---

## 4. Further Personal Config and Some References

Here's my simple instruction of [third_party utils I haved used](https://github.com/longjj/dotfiles/blob/master/scripts/Readme.md).

As for me, I still need to manually install `atom editor` and `Chinese Pinyin Input` after using this tool, maybe I will make it auto in the future. Some references below are in Chinese.

1. [New to manage dotfiles](https://sanctum.geek.nz/arabesque/managing-dot-files-with-git/)
2. [在ubuntu上配置拼音输入法](http://blog.csdn.net/luojj26/article/details/51859117)
3. [ubuntu 下源码编译vim的亲测方法](http://blog.csdn.net/luojj26/article/details/51338268)

----
## 5. My Config Result Overview
![config_result](https://github.com/longjj/dotfiles/blob/master/screenshot.png)

I hope it can give you help or inspiration!
