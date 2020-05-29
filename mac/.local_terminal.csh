#set path = (~/bin ~/.local/bin ~/Library/Haskell/bin /usr/local/bin /opt/local/bin /opt/local/sbin /bin /sbin /usr/bin /usr/sbin /usr/X11/bin)
set path = (~/bin ~/.local/bin /usr/local/bin /bin /sbin /usr/bin /usr/sbin /usr/X11/bin)
setenv	LD_LIBRARY_PATH	/home/kurokawa/lib:/usr/local/lib:/lib:/usr/lib

#unsetenv	LANG
#setenv	LANG	C
#setenv	LANG	ja_JP.eucJP
setenv	LANG	ja_JP.UTF-8
## force LANG C
#alias	man	'env LANG=C man'
#alias	make	'env LANG=C make'
#alias	svn	'env LANG=C svn' # error occurs

limit coredumpsize 32000

#setenv	LOCAL_ENV_LS_OPT	--show-control-chars
setenv	LOCAL_ENV_LS_OPT	""


### for mac ###
#alias emacs /Applications/Emacs.app/Contents/MacOS/Emacs
#alias emacs /Applications/MacPorts/EmacsMac.app/Contents/MacOS/Emacs
alias hsdoc /Library/Haskell/doc/index.html
alias diffmerge /Applications/DiffMerge.app/Contents/MacOS/DiffMerge
alias threadscope ~/Applications/threadscope.app/Contents/MacOS/threadscope
alias wireshark /Applications/Wireshark.app/Contents/MacOS/Wireshark


source ~/.tcshrc_complete
