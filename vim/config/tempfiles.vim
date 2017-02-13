" First of all, create these three folders:
" mkdir ~/.vim/tempfiles/.backup ~/.vim/tempfiles/.swp ~/.vim/tempfiles/.undo
" Now, put these lines in your vimrc file.

set undodir=~/.vim/tempfiles/.undo//
set backupdir=~/.vim/tempfiles/.backup//
set directory=~/.vim/tempfiles/.swp//

" the "//" at the end of each directory means that file names will be built from
" the complete path to the file with all path separators substituted to percent "%" sign.
" This will ensure file name uniqueness in the preserve directory.
