# Dotfiles Auto Setting
`Johnny Law`  `SYSU in Guangdong Province, China`

## 1. Overview

&ensp;&ensp;This repository contains my personal dotfiles and auto-setup tools through **python and bash** script. The master version is tested on **Ubuntu 16.04 LTS**. It may also work on other Debian or Ubuntu linux systems. When it goes to Mac, you may need to change some files in `/script` since I use `apt-get` to set the machine.

&ensp;&ensp;It is welcomed to fork and change it for yourself. All you need to change is the personal setting config. Replacing some config with utils you prefer, then you can **use it to easily set up** a personalized environment when you move to a new machine or when you reinstall the system. **I hope it can give all freshman an easy framework**.

&ensp;&ensp;If you can fork it and update it for more compatible (such as mac), I will appreciate your help. **I will also continue to update it.**

---

## 2. Usage

### 1) Pre request
- Install git, then execute this command in bash:`git clone https://github.com/longjj/dotfiles`
- Modify the `/scripts/setupGit.sh`,**<font size=5>set your own git global config.</font>**

### 2) Eexecute Commands
```bash
cd dotfiles
python setup.py [option]
```
###3) Option List:
1. `clean`: clean the old plugins and temp files dir in the repository, which is handy for developing.
2. `personalize`: After sensible setting, set your machine with your preference. (Please modify some scripts in `/scripts` to make your own personal settings)
With no option, it will config some basic tools.

###4) Basic Tools List:
1. vim (use [vundle](https://github.com/VundleVim/Vundle.vim) to manage plugins)
2. zsh (use [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) framework)
3. tmux (use [tpm](https://github.com/tmux-plugins/tpm) to manage plugins)

**<font size=5>For deep uses and config, please check their official documents</font>**

---

## 3. Notice

1. When config the icons, it is needed to add ppa to the system so you need to press enter to confirm timely, or it will be blocked.

---

## 4. Further Personal Config and Some References

As for me, I still need to manually install `atom editor` and `Chinese Pinyin Input` after using this tool, maybe I will make it auto in the future. Some references below are in Chinese.

1. [在ubuntu上配置拼音输入法](http://blog.csdn.net/luojj26/article/details/51859117)
2. [ubuntu 下源码编译vim的亲测方法](http://blog.csdn.net/luojj26/article/details/51338268)
3. [new to manage dotfiles](https://sanctum.geek.nz/arabesque/managing-dot-files-with-git/)
