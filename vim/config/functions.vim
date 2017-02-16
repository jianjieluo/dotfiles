" 将外部命令 wmctrl 控制窗口最大化的命令行参数封装成一个 vim 的函数
fun! ToggleFullscreen()
    call system("wmctrl -ir " . v:windowid . " -b toggle,fullscreen")
endf
" 全屏开/关快捷键
map <silent> <F11> :call ToggleFullscreen()<CR>

" ---------------------------------------------------------------------------
"clang-format
map <C-K> :pyf /usr/share/vim/addons/syntax/clang-format.py<cr>
imap <C-K> <c-o>:pyf /usr/share/vim/addons/syntax/clang-format.py<cr>

" ---------------------------------------------------------------------------
" Auto set author's information
" You can add the file type in the 2 help function to support the files you need.
"SET Comment START
autocmd BufNewFile *.py,*.js,*.cpp,*.sh exec ":call SetComment()" |normal 9Go

func SetComment()
	if expand("%:e") == 'py'
		call append(0, "#python file")
    let head = '#'
  elseif expand("%:e") == 'sh'
    call append(0, "#bash file")
    let head = '#'
	elseif expand("%:e") == 'js'
		call append(0, '//JavaScript file')
    let head = '//'
	elseif expand("%:e") == 'cpp'
		call append(0, '//C++ file')
    let head = '//'
	endif
	call append(1, head.'================================================')
	call append(2, head.'      Filename: '.expand("%"))
	call append(3, head)
	call append(4, head.'        Author: longj - luojj26@gmail.com')
	call append(5, head.'   Description: ---')
	call append(6, head.'   Head Create: '.strftime("%Y-%m-%d %H:%M:%S"))
	call append(7, head.' Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
	call append(8, head.'================================================')
endfunc

map <F2> :call SetComment()<CR>:9<CR>o
"SET Comment END

"Update last modified time and file name START

func UpdateData()
	if search ('Last Modified') != 0
    call cursor(8,1)
		let line = line('.')
    if &filetype == 'python'
      let head = '#'
    elseif &filetype == 'sh'
      let head = '#'
  	elseif &filetype == 'javascript'
      let head = '//'
  	elseif &filetype == 'cpp'
      let head = '//'
  	endif
		call setline(line, head.' Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
    " update file name
    call cursor(3,1)
    call setline(line('.'), head.'      Filename: '.expand("%"))
	endif
endfunc

autocmd FileWritePre,BufWritePre *.py,*.js,*.cpp,*.sh ks|call UpdateData()|'s

"Update last modified time and file name END
