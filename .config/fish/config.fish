function fish_prompt
   set_color --bold
   echo -n "[$HOST:"(prompt_pwd)"]% "
   set_color normal
end
set fish_prompt_pwd_dir_length 0

#alias	++	pushd
#alias	--	popd
alias	d	dirs
alias	j	jobs
alias	l	"ls -C --show-control-chars"
alias	la	"ls -aF --show-control-chars"
alias	ll	"ls -lF --show-control-chars"
alias	ls	"ls -F --show-control-chars"
alias	h	"history 40"
alias	hh	history
alias	hexdump	"hexdump -C"
alias	cp-f	"\cp -f"
alias	cp	'cp -i'
alias	ec	emacsclient
alias	lv	"lv -c"

alias	xterm	'xterm +tb'
alias	settitle	'echo -n "\033]0;\!:1" ; echo -n "\007"'
alias	cls	"echo -e '\\0033\\0143'"
alias	path_sed	'echo $PATH | sed "s/:/\n/g"'
alias	gpg_check	'gpg --list-only'
alias	mkdircd	'mkdir -p $1; cd $1'
alias	fmt_json	'python -mjson.tool'
alias	fmt_xml	'xmllint --format'

alias	rmbak	"rm *~ .*~ \#*\#"
alias	te	/cygdrive/c/files/Hidemaru/Hidemaru.exe
alias	psall	'ps -aux | grep kurokawa'

alias	zip	'zip -r'
alias	zip_pass	'zip -P'
alias	bz2	'bzip2 -dc $1 | tar xvf -'
alias	bz2t	'bzip2 -dc $1 | tar tvf -'
alias	enscript_hs	'enscript --highlight=haskell --color -C -o ~/tmp/out.html --language=html'
alias	enscript_cpp	'enscript --highlight=cpp --color -C -o ~/tmp/out.html --language=html'
alias	enscript_elisp	'enscript --highlight=elisp --color -C -o ~/tmp/out.html --language=html'
alias	enscript_sql	'enscript --highlight=sql --color -C -o ~/tmp/out.html --language=html'
alias	hasktags-r	'hasktags -e *.hs */*.hs */*/*.hs'
alias	cabal	"env LANG= cabal"
alias	stack	"env LANG= stack"


### svn ###
alias   lsco    "svn stat \!* | grep -v ^\?"
alias   lsup    "svn stat -u \!* | grep -v ^\?"
alias   rmtmpf  "svn stat --no-ignore \!* | grep ^\[\?\|I\] | cut -c 8- | xargs rm "
alias   rmtmpd  "svn stat --no-ignore \!* | grep ^\[\?\|I\] | cut -c 8- | xargs rm -rf "
alias   svn     "svn --non-interactive"



set LESS '--RAW-CONTROL-CHARS'  # -X is not needed because of my terminfo setting.
set PAGER 'lv -c'
