set fish_prompt_pwd_dir_length 0

function fish_prompt
   set_color --bold
   echo -n "[$HOST:"(prompt_pwd)"]% "
   set_color normal
end
