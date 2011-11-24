" Make vim not put the *.swp and backup files in the same directory
" as the file you're editing
if has('win16') || has('win32') || has('win64') || has('win95')
	set directory=c:\\temp
	set backupdir=c:\\temp
	set guifont=Consolas:h11:cANSI	" set gui font for windows
endif

" Actually disable these altogether - we probably don't need them
set nobackup
set nowritebackup
set noswapfile

set noshowmatch
set noerrorbells
set visualbell

" Treat these as part of the word, not dividers
set iskeyword=_,$,@,%,#,-

" Set the colour scheme
color darkblue

" Set mac gui font
if has('macunix') || has('mac')
	set guifont=Monaco:h12
endif

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

set nocompatible
"set showmatch
"set matchtime=3
set smartindent
set showcmd
set showmode
set tabstop=4
set shiftwidth=4
filetype plugin indent on
" don't add a space when Joining two lines
set nojoinspaces
" always show cursor position
set ruler
