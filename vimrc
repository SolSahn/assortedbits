" Basic appearance settings
colorscheme ron
syntax enable
set lazyredraw
set number
set ruler

" If gvim, sets theme to gruvbox and removes annoying toolbars
if has('gui_running')
  colorscheme gruvbox
  set background=dark
  set guioptions -=m
  set guioptions -=T
endif

" Indentation stuff
filetype indent on
set expandtab
set autoindent
set shiftwidth=2
set softtabstop=2
