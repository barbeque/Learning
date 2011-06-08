" Make vim not put the *.swp and backup files in the same directory
" as the file you're editing
set directory=c:\\temp
set backupdir=c:\\temp

" Actually disable these altogether - we probably don't need them
set nobackup
set nowritebackup

" Set the colour scheme
color slate

" Set the GUI font (for GVIM)
set guifont=Consolas:h11:cANSI

" Activate syntax for everything
syn on
" Switch on highlighting the last search pattern
set hlsearch

" Ignore a bunch of different binary types so I can't accidentally edit them
set wildignore=*.o,*.obj,*.bak,*.exe,*.dll

" I like case insensitive search; smartcase tells vim to pretend to be case
" insensitive UNLESS I specify a capital letter in my search, at which point
" it becomes case sensitive.
set smartcase

" line numbering
set nu!

" Tell vim that when it encounters a TT file, consider it to be a C# file
" for syntax highlighting purposes.
au BufNewFile,BufRead *.tt setfiletype cs
au BufNewFile,BufRead *.targets setfiletype xml
