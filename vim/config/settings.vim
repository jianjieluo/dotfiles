" Don’t show the intro message when starting Vim
set shortmess=atI
" Use UTF-8 without BOM
set encoding=utf-8 nobomb
" 关闭兼容模式
set nocompatible

" Allow cursor keys in insert mode
set esckeys
" Allow backspace in insert mode
set backspace=indent,eol,start
" Optimize for fast terminal connections
set ttyfast

" Show the filename in the window titlebar
set title
" Enhance command-line completion
set wildmenu

" 自动切换当前目录为当前文件所在的目录
set autochdir

" Always show status line
set laststatus=2
" Show the cursor position
set ruler
" Enable line numbers
set number
" Highlight current line and column
set cursorline
set cursorcolumn

" Highlight searches
set hlsearch
" Ignore case of searches
set ignorecase
" Highlight dynamically as pattern is typed
set incsearch

" Indentation.
set expandtab                         " Replace tabs with spaces.
set shiftwidth=4                      " Spaces used for autoindent and commands like >>.
set softtabstop=4                     " Spaces inserted by <Tab>.
set tabstop=4                         " Tabs used for autoindent and commands

" change the indetation when develop web program
autocmd BufNewFile,BufRead *.html,*.htm,*.css,*.js set noexpandtab tabstop=2 shiftwidth=2
autocmd BufNewFile,BufRead *.py set noexpandtab tabstop=4 shiftwidth=4
" Automatic commands
if has("autocmd")
	" Enable file type detection
	filetype on
	" Treat .json files as .js
	autocmd BufNewFile,BufRead *.json setfiletype json syntax=javascript
	" Treat .md files as Markdown
	autocmd BufNewFile,BufRead *.md setlocal filetype=markdown
endif

" Enable per-directory .vimrc files and disable unsafe commands in them
set exrc
set secure

" Enable mouse in all modes
set mouse=a
" Show the (partial) command as it’s being typed
set showcmd

" Reload file without prompting if it has changed on disk.
" Will still prompt if there is unsaved text in the buffer.
set autoread
" MacVim checks for autoread when it gains focus; terminal Vim
" must trigger checks. Do so when switching buffers, or after
" 2 secs (the value of updatetime) of pressing nothing.
set updatetime=2000
au WinEnter,BufWinEnter,CursorHold * silent! checktime
