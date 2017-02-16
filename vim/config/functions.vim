" 将外部命令 wmctrl 控制窗口最大化的命令行参数封装成一个 vim 的函数
fun! ToggleFullscreen()
    call system("wmctrl -ir " . v:windowid . " -b toggle,fullscreen")
endf
" 全屏开/关快捷键
map <silent> <F11> :call ToggleFullscreen()<CR>

"clang-format
map <C-K> :pyf /usr/share/vim/addons/syntax/clang-format.py<cr>
imap <C-K> <c-o>:pyf /usr/share/vim/addons/syntax/clang-format.py<cr>

" Auto set author's information
" You can add the file type in the 2 help function to support the files you need
"SET Comment START
autocmd BufNewFile *.py,*.js,*.cpp,*.sh exec ":call SetComment()" |normal 10Go

func SetComment()
	if expand("%:e") == 'py'
		call setline(1, "#python file")
    let head = '#'
  elseif expand("%:e") == 'sh'
    call setline(1, "#bash file")
    let head = '#'
	elseif expand("%:e") == 'js'
		call setline(1, '//JavaScript file')
    let head = '//'
	elseif expand("%:e") == 'cpp'
		call setline(1, '//C++ file')
    let head = '//'
	endif
	call append(1, head.'***********************************************')
	call append(2, head)
	call append(3, head.'      Filename: '.expand("%"))
	call append(4, head)
	call append(5, head.'        Author: longj - luojj26@gmail.com')
	call append(6, head.'   Description: ---')
	call append(7, head.'        Create: '.strftime("%Y-%m-%d %H:%M:%S"))
	call append(8, head.' Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
	call append(9, head.'***********************************************')
endfunc

map <F2> :call SetComment()<CR>:10<CR>o
"SET Comment END

"SET Last Modified Time START

func UpdateLastModifiedTime()
	call cursor(9,1)
	if search ('Last Modified') != 0
		let line = line('.')
    if expand("%:e") == 'py'
      let head = '#'
    elseif expand("%:e") == 'sh'
      let head = '#'
  	elseif expand("%:e") == 'js'
      let head = '//'
  	elseif expand("%:e") == 'cpp'
      let head = '//'
  	endif
		call setline(line, head.' Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
	endif
endfunc

autocmd FileWritePre,BufWritePre *.py,*.js,*.cpp,*.sh ks|call UpdateLastModifiedTime() |'s
"SET Last Modified Time END
