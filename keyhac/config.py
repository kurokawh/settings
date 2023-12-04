# -*- mode: python; coding: utf-8-dos -*-

##
## Windows の操作を emacs のキーバインドで行うための設定（keyhac版）
##

# このスクリプトは、keyhac で動作します。
#   https://sites.google.com/site/craftware/keyhac
# スクリプトですので、使いやすいようにカスタマイズしてご利用ください。
#
# この内容は、utf-8-dos の coding-system で config.py の名前でセーブして
# 利用してください。また、このスクリプトの最後の方にキーボードマクロの
# キーバインドの設定があります。英語キーボードと日本語キーボードで設定の
# 内容を変える必要があるので、利用しているキーボードに応じてコメントの
# 設定を変更してください。（現在の設定は、日本語キーボードとなっています。）
#
# emacs の挙動と明らかに違う動きの部分は以下のとおりです。
# ・ESC の二回押下で、ESC を入力できる。
# ・C-o と C-\ で IME の切り替えが行われる。
# ・C-c、C-z は、Windows の「コピー」、「取り消し」が機能するようにしている。
# ・C-x C-y で、クリップボード履歴を表示する。（C-n で選択を移動し、Enter で確定する）
# ・C-x o は、一つ前にフォーカスがあったウインドウに移動する。
#   NTEmacs から windowsアプリケーションソフトを起動した際に戻るのに便利。
# ・C-k を連続して実行しても、クリップボードへの削除文字列の蓄積は行われない。
#   C-u による行数指定をすると、削除行を一括してクリップボードに入れることができる。
# ・C-l は、アプリケーションソフト個別対応とする。recenter 関数で個別に指定すること。
#   この設定では、Sakura Editor のみ対応している。
# ・Excel の場合、^Enter に F2（セル編集モード移行）を割り当てている。

from time   import sleep
from keyhac import *

def configure(keymap):

    if 1:
        keymap.editor = "C:\\files\\Hidemaru\\Hidemaru.exe"
        #keymap.replaceKey( 28, 243 ) # 変換で IME on/off
        #keymap.replaceKey( 243, "Esc" ) # Esc <=> Kanji

        # emacs のキーバインドに"したくない"アプリケーションソフトを指定する（False を返す）
        # keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます
        def is_emacs_target(window):
            if window.getProcessName() in ("cmd.exe",            # cmd
                                           # "explorer.exe",       # explorer
                                           # "POWERPNT.EXE",       # power point
                                           "mstsc.exe",          # Remote Desktop
                                           "KeePass.exe",        # KeePass
                                           "emacs-X11.exe",      # Emacs-X11
                                           "emacs.exe",          # Emacs
                                           "XWin.exe",           # Cygwin/X
                                           "putty.exe",          # PuTTY
                                           "ttermpro.exe",       # TeraTerm
                                           "TurboVNC.exe",       # TurboVNC
                                           "vncviewer.exe",      # UltraVNC
                                           "mintty.exe",         # mintty
                                           "gvim.exe",           # GVim
                                           # "eclipse.exe",        # Eclipse
                                           "xyzzy.exe",          # xyzzy
                                           "VirtualBox.exe",     # VirtualBox
                                           "Xming.exe",          # Xming
                                           "MobaXterm.exe"):     # MobaXterm
                return False
            # 以下の様に classname で指定する方法もあるが、上記の processname による指定の方法に統一した
            # if window.getClassName()   in ("mintty",             # mintty
            #                                "Emacs",              # Emacs
            #                                "Vim"):               # GVim
            #     return False
            return True

        # input method の切り替え"のみをしたい"アプリケーションソフトを指定する（True を返す）
        # 指定できるアプリケーションソフトは、is_emacs_target で除外指定したものからのみとする
        def is_im_target(window):
            if window.getProcessName() in ("cmd.exe",            # cmd
                                           "mintty.exe",         # mintty
                                           "gvim.exe",           # GVim
                                           # "eclipse.exe",        # Eclipse
                                           "xyzzy.exe",          # xyzzy
                                           "putty.exe",          # PuTTY
                                           "ttermpro.exe",       # TeraTerm
                                           "MobaXterm.exe"):     # MobaXterm
                return True
            # 以下の様に classname で指定する方法もあるが、上記の processname による指定の方法に統一した
            # if window.getClassName()   in ("mintty",             # mintty
            #                                "Vim"):               # GVim
            #     return True
            return False

        keymap_emacs = keymap.defineWindowKeymap(check_func=is_emacs_target)
        keymap_im = keymap.defineWindowKeymap(check_func=is_im_target)

        # mark がセットされると True になる
        keymap_emacs.is_mark = False

        # universal-argument コマンドが実行されると True になる
        keymap_emacs.is_universal_argument = False

        # universal-argument コマンドが実行された後に数字が入力されると True になる
        keymap_emacs.is_digit = False

        # コマンドのリピート回数を設定する
        keymap_emacs.repeat_count = 1

        ### kuro ===>
        # アプリケーションデフォルトのショートカットキーを利用する目的で、
        # +SHIFT で、デフォルトショートカットキーとするアプリのリスト。
        # 例： POWERPOINT.EXE では C-b は左移動ではなく、強調文字設定したいので
        # S-C-b を C-b に割り当てる。 主に ctrl_shift_?() 向け。
        def is_default_shortcut_requested(window):
            if (window.getProcessName() in ("POWERPNT.EXE",       # power point
                                            "EXCEL.EXE",          # excel
                                            "WINWORD.EXE",        # word
                                            "firefox.exe")) \
            or is_onenote(window) \
            or is_chrome(window):                             # corome
                return True
            return False
        def is_onenote(window):
            return window.getProcessName() == "onenoteim.exe" \
                or window.getProcessName() == "ONENOTE.EXE" # OneNote
        def is_chrome(window):
            return window.getClassName() == "Chrome_WidgetWin_1" # chrome


        def forward_word():
            keymap.InputKeyCommand("C-Right")()
        def backward_word():
            keymap.InputKeyCommand("C-Left")()
        def replace_string():
            keymap.InputKeyCommand("C-h")()
        def delete_word():
            keymap.InputKeyCommand("C-S-Right")()
            kill_region()
            keymap_emacs.is_mark = False
        def delete_backward_word():
            keymap.InputKeyCommand("C-S-Left")()
            kill_region()
            keymap_emacs.is_mark = False
        def transpose_chars(): # C-t
            keymap.InputKeyCommand("S-Left")()
            kill_region()
            keymap.InputKeyCommand("Right")()
            keymap.InputKeyCommand("C-v")()
            keymap_emacs.is_mark = False
        def jump_to_line(): 
            keymap.InputKeyCommand("C-g")()
        def search_next(): 
            window = keymap.getWindow()
            if is_chrome(window):   # chrome
                keymap.InputKeyCommand("C-g")()
            #VS or FireFox
            if window.getProcessName() == "devenv.exe" \
               or window.getProcessName() == "firefox.exe":
                keymap.InputKeyCommand("F3")()
            else:
                keymap.InputKeyCommand("A-n")() # same as defult for other apps
        def search_prev(): 
            window = keymap.getWindow()
            if is_chrome(window):   # chrome
                keymap.InputKeyCommand("C-S-g")()
            #VS or FireFox
            if window.getProcessName() == "devenv.exe" \
               or window.getProcessName() == "firefox.exe":
                keymap.InputKeyCommand("S-F3")()
            else:
                keymap.InputKeyCommand("A-p")() # same as defult for other apps
        def ctrl_m():
            if is_default_shortcut_requested(keymap.getWindow()):
                # disable newline in order to insert new slide with C-m
                keymap.InputKeyCommand("C-m")()
            else:
                keymap.InputKeyCommand("Enter")()
            keymap_emacs.is_mark = False
        def ctrl_shift_5():
            window = keymap.getWindow()
            # use C-S-5 to STRIKETHROUGH
            if is_onenote(window): # one note ***
                keymap.InputKeyCommand("C-Minus")()
            elif is_chrome(window):            # chrome (for googledoc not for confluence) ***
                keymap.InputKeyCommand("A-S-5")()
            elif is_default_shortcut_requested(keymap.getWindow()): # *NOTE* onenote & chrome must ahead because is_default_shortcut_requested() contains them
                keymap.InputKeyCommand("Alt", "h", "4")()
            else:
                keymap.InputKeyCommand("C-S-5")()
        def ctrl_shift_a():
            keymap.InputKeyCommand("S-Home")()
        def ctrl_shift_b():
            # use C-S-b to BOLD FONT instead of C-b.
            if is_default_shortcut_requested(keymap.getWindow()):
                keymap.InputKeyCommand("C-b")()
            else:
                keymap.InputKeyCommand("C-S-b")()
        def alt_shift_d():
            keymap.InputKeyCommand("A-d")()
        def ctrl_shift_e():
            keymap.InputKeyCommand("S-End")()
            if keymap.getWindow().getClassName() == "_WwG": # Microsoft Word
                if keymap_emacs.is_mark:
                    keymap.InputKeyCommand("Left-S")()
        def ctrl_shift_h():
            keymap.InputKeyCommand("C-h")()
        def ctrl_shift_k():
            # link
            if keymap.getWindow().getProcessName() == "slack.exe":
                keymap.InputKeyCommand("C-S-u")()
            elif is_default_shortcut_requested(keymap.getWindow()):
                keymap.InputKeyCommand("C-k")()
            else:
                keymap.InputKeyCommand("C-S-k")()
        def ctrl_shift_p():
            keymap.InputKeyCommand("C-p")()
        def alt_shift_s():
            if keymap.getWindow().getProcessName() == "devenv.exe":
                keymap.InputKeyCommand("A-S-s")()
            else:
                write_file()()
        def ctrl_shift_t():
            keymap.InputKeyCommand("C-t")()
        def ctrl_shift_u():
            keymap.InputKeyCommand("C-u")()
        def ctrl_shift_y():
            keymap.InputKeyCommand("C-S-v")()
        def ctrl_shift_ob():
            keymap.InputKeyCommand("C-OpenBracket")()
        def ctrl_shift_cb():
            keymap.InputKeyCommand("C-CloseBracket")()
        ### <=== kuro

        ########################################################################
        # IMEの切替え
        ########################################################################

        def toggle_input_method():
            # keymap.InputKeyCommand("A-BackQuote")()
            keymap.InputKeyCommand("(243)")()

        ########################################################################
        # ファイル操作
        ########################################################################

        def find_file():
            keymap.InputKeyCommand("C-o")()
            keymap_emacs.is_mark = False

        def save_buffer():
            keymap.InputKeyCommand("C-s")()

        def write_file():
            if keymap.getWindow().getClassName() == "Internet Explorer_Server":
                # for Internet Explorer
                keymap.InputKeyCommand("C-s")()
            else:
                keymap.InputKeyCommand("A-f", "A-a")()

        ########################################################################
        # カーソル移動 
        ########################################################################

        def forward_char():
            keymap.InputKeyCommand("Right")()

        def backward_char():
            keymap.InputKeyCommand("Left")()

        def next_line():
            keymap.InputKeyCommand("Down")()

        def previous_line():
            keymap.InputKeyCommand("Up")()

        def move_beginning_of_line():
            keymap.InputKeyCommand("Home")()

        def move_end_of_line():
            keymap.InputKeyCommand("End")()
            if keymap.getWindow().getClassName() == "_WwG": # Microsoft Word
                if keymap_emacs.is_mark:
                    keymap.InputKeyCommand("Left")()

        def beginning_of_buffer():
            keymap.InputKeyCommand("C-Home")()

        def end_of_buffer():
            keymap.InputKeyCommand("C-End")()

        def scroll_up():
            keymap.InputKeyCommand("PageUp")()

        def scroll_down():
            keymap.InputKeyCommand("PageDown")()

        def recenter():
            if keymap.getWindow().getClassName() == "EditorClient": # Sakura Editor
                keymap.InputKeyCommand("C-h")()
            if keymap.getWindow().getClassName() == "HM32CLIENT": # Hidemaru Editor
                keymap.InputKeyCommand("C-l")()

        ########################################################################
        # カット / コピー / 削除 / アンドゥ
        ########################################################################

        def delete_backward_char():
            keymap.InputKeyCommand("Back")()
            keymap_emacs.is_mark = False

        def delete_char():
            keymap.InputKeyCommand("Delete")()
            keymap_emacs.is_mark = False

        def kill_line():
            keymap_emacs.is_mark = True
            mark(move_end_of_line)()
            keymap.InputKeyCommand("C-x")()
            keymap_emacs.is_mark = False

        def kill_line2():
            if keymap_emacs.repeat_count == 1:
                kill_line()
            else:
                keymap_emacs.is_mark = True
                if keymap.getWindow().getClassName() == "_WwG": # Microsoft Word
                    for i in range(keymap_emacs.repeat_count):
                        mark(next_line)()
                    mark(move_beginning_of_line)()
                else:
                    for i in range(keymap_emacs.repeat_count - 1):
                        mark(next_line)()
                    mark(move_end_of_line)()
                    mark(forward_char)()
                kill_region()
                keymap_emacs.is_mark = False

        def kill_region():
            keymap.InputKeyCommand("C-x")()
            keymap_emacs.is_mark = False

        def kill_ring_save():
            keymap.InputKeyCommand("C-c")()
            # Microsoft Excel/Word(outlook) 以外
            if not is_default_shortcut_requested(keymap.getWindow()):
                # 選択されているリージョンのハイライトを解除するために Esc を発行しているが、
                # アプリケーションソフトによっては効果なし
                keymap.InputKeyCommand("Esc")()
            keymap_emacs.is_mark = False

        def windows_copy():
            keymap.InputKeyCommand("C-c")()
            keymap_emacs.is_mark = False

        def yank():
            keymap.InputKeyCommand("C-v")()
            keymap_emacs.is_mark = False

        def undo():
            keymap.InputKeyCommand("C-z")()
            keymap_emacs.is_mark = False

        def redo():
            keymap.InputKeyCommand("C-y")()
            keymap_emacs.is_mark = False

        def set_mark_command():
            if keymap_emacs.is_mark:
                keymap_emacs.is_mark = False
            else:
                keymap_emacs.is_mark = True

        def mark_whole_buffer():
            if keymap.getWindow().getClassName() == "DirectUIHWND": # Explorer
                # use C-a to select all for Explorer because C-End + C-S-Home fails
                keymap.InputKeyCommand("C-a")()
                keymap_emacs.is_mark = True
            else:
                keymap.InputKeyCommand("C-End", "C-S-Home")()
                keymap_emacs.is_mark = True

# same as mark_whole_buffer
#        def mark_page():
#            keymap.InputKeyCommand("C-End", "C-S-Home")()
#            keymap_emacs.is_mark = True

        def open_line():
            keymap.InputKeyCommand("Enter", "Up", "End")()
            keymap_emacs.is_mark = False

        ########################################################################
        # バッファ / ウインドウ操作 
        ########################################################################

        def kill_buffer():
            if keymap.getWindow().getClassName() == "HM32CLIENT": # Hidemaru Editor
                kill_emacs()
            else:
                keymap.InputKeyCommand("C-F4")()
                keymap_emacs.is_mark = False

        def other_window():
            keymap.InputKeyCommand("D-ALT")()
            keymap.InputKeyCommand("Tab")()
            sleep(0.01)
            keymap.InputKeyCommand("U-ALT")()
            keymap_emacs.is_mark = False

        ########################################################################
        # 文字列検索 / 置換 
        ########################################################################

        def isearch_forward():
            keymap.InputKeyCommand("C-f")()
            keymap_emacs.is_mark = False

        def isearch_backward():
            keymap.InputKeyCommand("C-f")()
            keymap_emacs.is_mark = False

        ########################################################################
        # キーボードマクロ
        ########################################################################

        def kmacro_start_macro():
            keymap.command_RecordStart()

        def kmacro_end_macro():
            keymap.command_RecordStop()
            # キーボードマクロの終了キー C-x ) の C-x がマクロに記録されてしまうのを削除する
            # キーボードマクロの終了キーの前提を C-x ) としていることについては、とりえず了承ください
            if len(keymap.record_seq) > 0 and keymap.record_seq[len(keymap.record_seq) - 1] == (162, True):
                keymap.record_seq.pop()
                if len(keymap.record_seq) > 0 and keymap.record_seq[len(keymap.record_seq) - 1] == (88, True):
                    keymap.record_seq.pop()
                    if len(keymap.record_seq) > 0 and keymap.record_seq[len(keymap.record_seq) - 1] == (88, False):
                        keymap.record_seq.pop()
                        if len(keymap.record_seq) > 0 and keymap.record_seq[len(keymap.record_seq) - 1] == (162, False):
                            for i in range(len(keymap.record_seq) - 1, -1, -1):
                                if keymap.record_seq[i] == (162, False):
                                    keymap.record_seq.pop()
                                else:
                                    break
                        else:
                            # コントロール系の入力が連続して行われる場合があるための対処
                            keymap.record_seq.append((162, True))

        def kmacro_end_and_call_macro():
            keymap.command_RecordPlay()

        ########################################################################
        # その他
        ########################################################################

        def newline():
            keymap.InputKeyCommand("Enter")()
            keymap_emacs.is_mark = False

        def newline_and_indent():
            keymap.InputKeyCommand("Enter", "Tab")()
            keymap_emacs.is_mark = False

        def ctrl_i():
            if keymap.getWindow().getClassName() == "HM32CLIENT": # Hidemaru Editor
                keymap.InputKeyCommand("C-i")()
            else:
                indent_for_tab_command()

        def indent_for_tab_command():
            keymap.InputKeyCommand("Tab")()
            keymap_emacs.is_mark = False

        def keybord_quit():
            # Microsoft Excel/Word(outlook) 以外
            if not is_default_shortcut_requested(keymap.getWindow()):
                # 選択されているリージョンのハイライトを解除するために Esc を発行しているが、
                # アプリケーションソフトによっては効果なし
                keymap.InputKeyCommand("Esc")()
            keymap.command_RecordStop()
            keymap_emacs.is_mark = False

        def kill_emacs():
            keymap.InputKeyCommand("A-F4")()
            keymap_emacs.is_mark = False

        def universal_argument():
            if is_chrome(keymap.getWindow()):   # chrome
                keymap.InputKeyCommand("C-u")() # display source
            else:
                keymap_emacs.is_universal_argument = True
                keymap_emacs.repeat_count = keymap_emacs.repeat_count * 4

        def clipboard_list():
            keymap_emacs.is_mark = False
            keymap.command_ClipboardList()

        ########################################################################
        # 共通関数
        ########################################################################

        def digit(number):
            def _digit():
                if keymap_emacs.is_universal_argument == True:
                    if keymap_emacs.is_digit == True:
                        keymap_emacs.repeat_count = keymap_emacs.repeat_count * 10 + number
                    else:
                        keymap_emacs.repeat_count = number
                        keymap_emacs.is_digit = True
                else:
                    repeat(keymap.InputKeyCommand(str(number)))()
            return _digit

        def mark(func):
            def _mark():
                if keymap_emacs.is_mark:
                    # D-Shift だと、M-< や M-> 押下時に、D-Shift が解除されてしまう。その対策。
                    keymap.InputKeyCommand("D-LShift")()
                    keymap.InputKeyCommand("D-RShift")()
                func()
                if keymap_emacs.is_mark:
                    keymap.InputKeyCommand("U-LShift")()
                    keymap.InputKeyCommand("U-RShift")()
            return _mark

        def reset_mark(func):
            def _reset_mark():
                func()
                keymap_emacs.is_mark = False
            return _reset_mark

        def reset(func):
            def _reset():
                func()
                keymap_emacs.is_universal_argument = False
                keymap_emacs.is_digit = False
                keymap_emacs.repeat_count = 1
            return _reset

        def repeat(func):
            def _repeat():
                for i in range(keymap_emacs.repeat_count):
                    func()
            return reset(_repeat)

        def repeat2(func):
            def _repeat2():
                if keymap_emacs.is_mark == True:
                    keymap_emacs.repeat_count = 1
                repeat(func)()
            return _repeat2

        ########################################################################
        # キーバインド
        ########################################################################

        # http://www.azaelia.net/factory/vk.html

        # 0-9
        for vkey in range(48, 57 + 1):
            keymap_emacs["S-(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand("S-(" + str(vkey) + ")")))

        # SPACE, A-Z
        for vkey in [32] + list(range(65, 90 + 1)):
            keymap_emacs[  "(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand(  "(" + str(vkey) + ")")))
            keymap_emacs["S-(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand("S-(" + str(vkey) + ")")))

        # 10 key の特殊文字
        for vkey in [106, 107, 109, 110, 111]:
            keymap_emacs[  "(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand(  "(" + str(vkey) + ")")))

        # 特殊文字
        for vkey in list(range(186, 192 + 1)) + list(range(219, 222 + 1)) + [226]:
            keymap_emacs[  "(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand(  "(" + str(vkey) + ")")))
            keymap_emacs["S-(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand("S-(" + str(vkey) + ")")))

        keymap_emacs["C-q"] = keymap.defineMultiStrokeKeymap("C-q")
        for vkey in range(256):
            keymap_emacs["C-q"][  "(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand(  "(" + str(vkey) + ")")))
            keymap_emacs["C-q"]["S-(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand("S-(" + str(vkey) + ")")))
            keymap_emacs["C-q"]["C-(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand("C-(" + str(vkey) + ")")))
            keymap_emacs["C-q"]["A-(" + str(vkey) + ")"] = reset_mark(repeat(keymap.InputKeyCommand("A-(" + str(vkey) + ")")))

        for key in range(10):
            keymap_emacs[str(key)]      = digit(key)

        keymap_emacs["C-Yen"]           = toggle_input_method
        keymap_emacs["C-o"]             = toggle_input_method # or open_line
        keymap_im["C-Yen"]              = toggle_input_method
        keymap_im["C-o"]                = toggle_input_method

        keymap_emacs["C-u"]             = universal_argument

        keymap_emacs["C-b"]             = repeat(mark(backward_char))
        keymap_emacs["C-f"]             = repeat(mark(forward_char))
        keymap_emacs["C-n"]             = repeat(mark(next_line))
        keymap_emacs["C-p"]             = repeat(mark(previous_line))

        keymap_emacs["C-d"]             = repeat2(delete_char)
        keymap_emacs["C-h"]             = repeat2(delete_backward_char)

        keymap_emacs["C-Space"]         = reset(set_mark_command)
        keymap_emacs["C-Slash"]         = reset(undo)
        keymap_emacs["C-S-Slash"]       = reset(redo)
        keymap_emacs["C-Atmark"]        = reset(set_mark_command)
        keymap_emacs["C-Underscore"]    = reset(undo)
        keymap_emacs["C-a"]             = reset(mark(move_beginning_of_line))
#        keymap_emacs["C-c"]             = reset(windows_copy)
        keymap_emacs["C-e"]             = reset(mark(move_end_of_line))
        keymap_emacs["C-g"]             = reset(keybord_quit)
        keymap_emacs["C-i"]             = repeat(ctrl_i)
        keymap_emacs["Tab"]             = repeat(indent_for_tab_command)
#        keymap_emacs["C-j"]             = reset(newline_and_indent)
        keymap_emacs["C-k"]             = reset(kill_line2)
        keymap_emacs["C-l"]             = reset(recenter)
        keymap_emacs["C-m"]             = repeat(ctrl_m)
        keymap_emacs["Enter"]           = repeat(newline)
        keymap_emacs["C-r"]             = reset(isearch_backward)
        keymap_emacs["C-s"]             = reset(isearch_forward)
        keymap_emacs["C-v"]             = reset(mark(scroll_down))
        keymap_emacs["C-w"]             = reset(kill_region)
        keymap_emacs["C-y"]             = reset(yank)
#        keymap_emacs["C-z"]             = reset(undo)
#        keymap_emacs["C-S-z"]           = reset(redo)

        keymap_emacs["A-S-Comma"]       = reset(mark(beginning_of_buffer))
        keymap_emacs["A-S-Period"]      = reset(mark(end_of_buffer))
        keymap_emacs["A-v"]             = reset(mark(scroll_up))
        keymap_emacs["A-w"]             = reset(kill_ring_save)

        #keymap_emacs["Esc"]             = keymap.defineMultiStrokeKeymap("Esc")
        #keymap_emacs["Esc"]["Esc"]      = reset(keymap.InputKeyCommand("Esc"))
        #keymap_emacs["Esc"]["S-Comma"]  = reset(mark(beginning_of_buffer))
        #keymap_emacs["Esc"]["S-Period"] = reset(mark(end_of_buffer))
        #keymap_emacs["Esc"]["v"]        = reset(mark(scroll_up))
        #keymap_emacs["Esc"]["w"]        = reset(kill_ring_save)

        keymap_emacs["C-OpenBracket"]                  = keymap.defineMultiStrokeKeymap("C-OpenBracket")
        keymap_emacs["C-OpenBracket"]["C-OpenBracket"] = reset(keymap.InputKeyCommand("Esc"))
        keymap_emacs["C-OpenBracket"]["S-Comma"]       = reset(mark(beginning_of_buffer))
        keymap_emacs["C-OpenBracket"]["S-Period"]      = reset(mark(end_of_buffer))
        keymap_emacs["C-OpenBracket"]["v"]             = reset(mark(scroll_up))
        keymap_emacs["C-OpenBracket"]["w"]             = reset(kill_ring_save)

        keymap_emacs["C-x"]             = keymap.defineMultiStrokeKeymap("C-x")
        keymap_emacs["C-x"]["C-c"]      = reset(kill_emacs)
        keymap_emacs["C-x"]["C-f"]      = reset(find_file)
        keymap_emacs["C-x"]["C-p"]      = reset(mark_whole_buffer)
        keymap_emacs["C-x"]["C-s"]      = reset(save_buffer)
        keymap_emacs["C-x"]["C-w"]      = reset(write_file)
        keymap_emacs["C-x"]["C-y"]      = reset(clipboard_list)
        keymap_emacs["C-x"]["h"]        = reset(mark_whole_buffer)
        keymap_emacs["C-x"]["k"]        = reset(kill_buffer)
        keymap_emacs["C-x"]["o"]        = reset(other_window)
        keymap_emacs["C-x"]["u"]        = reset(undo)

        # キーボードマクロ（英語キーボードの場合）
        # keymap_emacs["C-x"]["S-9"]      = kmacro_start_macro
        # keymap_emacs["C-x"]["S-0"]      = kmacro_end_macro

        # キーボードマクロ（日本語キーボードの場合）
        keymap_emacs["C-x"]["S-8"]      = kmacro_start_macro
        keymap_emacs["C-x"]["S-9"]      = kmacro_end_macro

        # キーボードマクロ（共通）
        keymap_emacs["C-x"]["e"]        = repeat(kmacro_end_and_call_macro)

        # for Excel
        keymap_excel = keymap.defineWindowKeymap(class_name='EXCEL*')
        # C-Enter 押下で、「セル編集モード移行」に入る
        keymap_excel["C-Enter"] = reset(keymap.InputKeyCommand("F2"))


        ### kuro ===>
        keymap_emacs["A-b"]             = repeat(mark(backward_word))
        keymap_emacs["A-f"]             = repeat(mark(forward_word))
        keymap_emacs["A-d"]             = reset(delete_word)
        keymap_emacs["C-Back"]          = reset(delete_backward_word)
        keymap_emacs["C-t"]             = reset(transpose_chars)
        keymap_emacs["A-r"]             = repeat(mark(replace_string))
        keymap_emacs["A-g"]             = reset(jump_to_line)
        keymap_emacs["A-n"]             = reset(search_next)
        keymap_emacs["A-p"]             = reset(search_prev)
        #keymap_emacs["A-%"]             = repeat(mark(replace_string))
        keymap_emacs["C-S-5"]           = repeat(mark(ctrl_shift_5))
        keymap_emacs["C-S-a"]           = repeat(mark(ctrl_shift_a))
        keymap_emacs["C-S-b"]           = repeat(mark(ctrl_shift_b))
        keymap_emacs["C-S-e"]           = repeat(mark(ctrl_shift_e))
        keymap_emacs["C-S-h"]           = repeat(mark(ctrl_shift_h))
        keymap_emacs["C-S-k"]           = repeat(mark(ctrl_shift_k))
        keymap_emacs["C-S-p"]           = repeat(mark(ctrl_shift_p))
        keymap_emacs["C-S-t"]           = repeat(mark(ctrl_shift_t))
        keymap_emacs["C-S-y"]           = repeat(mark(ctrl_shift_y))
        keymap_emacs["C-S-s"]           = reset(save_buffer)
        keymap_emacs["C-S-u"]           = repeat(mark(ctrl_shift_u))
        keymap_emacs["C-S-OpenBracket"]           = repeat(mark(ctrl_shift_ob))
        keymap_emacs["C-S-CloseBracket"]           = repeat(mark(ctrl_shift_cb))
        keymap_emacs["A-S-C"]           = reset(windows_copy) # for error code viewer
        keymap_emacs["A-S-s"]           = reset(mark(alt_shift_s))

        keymap_emacs["C-c"]             = keymap.defineMultiStrokeKeymap("C-c")
        keymap_emacs["C-c"]["C-c"]      = repeat(mark(alt_shift_d)) # for visual souce code
        keymap_emacs["A-S-d"]           = repeat(mark(alt_shift_d))
        ### <===

