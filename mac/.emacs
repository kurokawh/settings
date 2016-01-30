;; Red Hat Linux default .emacs initialization file

;; Are we running XEmacs or Emacs?
(defvar running-xemacs (string-match "XEmacs\\|Lucid" emacs-version))

;; Set up the keyboard so the delete key on both the regular keyboard
;; and the keypad delete the character under the cursor and to the right
;; under X, instead of the default, backspace behavior.
;(global-set-key [delete] 'delete-char)
;(global-set-key [kp-delete] 'delete-char)

;; Turn on font-lock mode for Emacs
(cond ((not running-xemacs)
       (global-font-lock-mode t)
))

;; Always end a file with a newline
(setq require-final-newline t)

;; Stop at the end of the file, not just add lines
(setq next-line-add-newlines nil)

;; Enable wheelmouse support by default
;(if (not running-xemacs)
;    (require 'mwheel) ; Emacs
;  (mwheel-install) ; XEmacs
;)


(line-number-mode t)
(menu-bar-mode nil) ; disable menu bar
(tool-bar-mode nil) ; disable tool bar

; swap C-h
;(load "term/keyswap")


(add-hook 'c-mode-common-hook
	  '(lambda ()
	     (c-set-style "cc-mode")
	     (set-variable (quote tab-width) 4)))

;; C++ style
(add-hook 'c++-mode-hook
	  '(lambda()
	     (set-variable (quote tab-width) 4)
	     (c-set-style "cc-mode")))
;             (c-set-style "bsd")))
;             (c-set-style "k&r")))
;             (c-set-style "ellemtel")))

;;; for ruby ;;;
;(require 'refe)
(load "rrse")
(rrse-setup)
(add-hook 'ruby-mode-hook
	  '(lambda ()
	     (setq tab-width 4)
	     (setq indent-tabs-mode 't)
	     (setq ruby-indent-level tab-width)
	     (define-key ruby-mode-map [f1] 'rrse-help)
	     (define-key ruby-mode-map "\C-j" 'goto-line)))
(load "rubydb3x")

;;; subversion psvn ;;;
(require 'psvn)
;; Start the svn interface with M-x svn-status


;;; for csharp ;;;
(load "csharp-mode")


;;;; for gdb ;;;;
(add-hook 'gud-mode-hook
	  '(lambda()
	     (global-set-key (quote [f3]) (quote gud-find-c-expr))
	     (global-set-key (quote [f4]) (quote gud-print))
	     (global-set-key (quote [f5]) (quote gud-cont))
	     (global-set-key (quote [f9]) (quote gud-break))
	     (global-set-key (quote [S-f9]) (quote gud-remove))
	     (global-set-key (quote [f10]) (quote gud-next))
	     (global-set-key (quote [f11]) (quote gud-step))
	     (global-set-key (quote [S-f11]) (quote gud-finish))
	     (global-set-key (quote [prior]) (quote gud-up))
	     (global-set-key (quote [next]) (quote gud-down))
	     (global-set-key (quote [home]) (quote gud-display-frame))))


;;;; global ;;;;
;(global-set-key "\C-J" (quote goto-line))
(global-set-key "\362" (quote replace-string))
(global-set-key "" (quote revert-buffer))
(global-set-key "\C-h" (quote delete-backward-char))
(global-set-key (kbd "M-%") 'vr/query-replace)
(global-set-key [zenkaku-hankaku] (quote toggle-input-method))

(setq default-major-mode 'text-mode)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
; '(haskell-mode-hook (quote (turn-on-haskell-indent)))
 '(safe-local-variable-values (quote ((haskell-process-use-ghci . t) (haskell-indent-spaces . 4))))
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(setq inhibit-startup-message t)

;;; cua-mode ;;;
;; http://tech.kayac.com/archive/emacs-rectangle.html
(cua-mode t)
(setq cua-enable-cua-keys nil) ; そのままだと C-x が切り取りになってしまったりするので無効化

;;; package.el ;;;
(require 'package)
;; MELPAを追加
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/") t)
;; MELPA-stableを追加
(add-to-list 'package-archives '("melpa-stable" . "http://stable.melpa.org/packages/") t)
;; Marmaladeを追加
(add-to-list 'package-archives  '("marmalade" . "http://marmalade-repo.org/packages/") t)
;; Orgを追加
(add-to-list 'package-archives '("org" . "http://orgmode.org/elpa/") t)
(package-initialize)

;;; auto-install.el ;;;
(require 'auto-install)
(auto-install-update-emacswiki-package-name t) ; EmacsWikiからパッケージ名を取得
;(auto-install-compatibility-setup)
(add-to-list 'load-path "~/.emacs.d/auto-install")

;;; emacs-zissen ===>
;; auto-complete
(when (require 'auto-complete-config nil t)
  (add-to-list 'ac-dictionary-directories
	       "~/.emacs.d/elisp/ac-dict")
  (setq ac-auto-show-menu nil) ; disable auto show menu
;  (define-key ac-mode-map (kbd "M-/") 'auto-complete) ; (override default completion)
  (define-key ac-mode-map (kbd "M-?") 'auto-complete) ; S-M-/ pops up candidates
  (ac-config-default))

;; setting of color_moccur
(when (require 'color-moccur nil t)
  ;; assign occur-by-moccur to M-o.
  (define-key global-map (kbd "M-o") 'occur-by-moccur)
  ;; AND search with space
  ;(setq moccur-split-word t)
  ;; ignore in directory search
  (add-to-list 'dmoccur-exclusion-mask "\\.DS_Store")
  (add-to-list 'dmoccur-exclusion-mask "^#.+#$")
  ;; use Migemo if it is available.
  (when (and (executable-find "cmigemo")
	     (require 'migemo nil t))
    (setq moccur-use-migemo t))
  ;; load moccur-edit as well.
  (require 'moccur-edit nil t))

;; settings of wgrep
(require 'wgrep nil t)

;; setting of undo-tree
;; C-x u shows undo tree.
(when (require 'undo-tree nil t)
  (global-undo-tree-mode))

;;; <=== emacs zissen


;;; anything.el ;;;
;(require 'anything-startup)

;;; haskell-mode.el ;;;
;;; from http://d.hatena.ne.jp/kitokitoki/20111217/p1
(require 'haskell-mode)
(require 'haskell-cabal)
(add-to-list 'auto-mode-alist '("\\.hs$" . haskell-mode))
(add-to-list 'auto-mode-alist '("\\.lhs$" . literate-haskell-mode))
(add-to-list 'auto-mode-alist '("\\.cabal\\'" . haskell-cabal-mode))
(add-hook 'haskell-mode-hook (lambda () (turn-on-haskell-indent)))
;; ghc-mod
;; cabal でインストールしたライブラリのコマンドが格納されている bin ディレクトリへのパスを exec-path に追加する
;(add-to-list 'exec-path (concat (getenv "HOME") "/.cabal/bin"))
;; ghc-flymake.el などがあるディレクトリ ghc-mod を ~/.emacs.d 以下で管理することにした
;(add-to-list 'load-path "~/.emacs.d/elisp/ghc-mod") 
;(add-to-list 'load-path "~/Library/Haskell/ghc-7.6.3/lib/ghc-mod-3.1.7/share") 
;(add-to-list 'load-path "~/Library/Haskell/ghc-7.6.3/lib/hlint-1.8.59/share")
(add-to-list 'load-path "~/.stack/global-project/.stack-work/install/x86_64-osx/lts-3.10/7.10.2/share/x86_64-osx-ghc-7.10.2/ghc-mod-5.4.0.0/elisp") 
(add-to-list 'load-path "~/.stack/snapshots/x86_64-osx/lts-3.10/7.10.2/share/x86_64-osx-ghc-7.10.2/hlint-1.9.21")
(autoload 'ghc-init "ghc" nil t)
;(autoload 'ghc-debug "ghc" nil t) ; by kuro from http://www.mew.org/~kazu/proj/ghc-mod/en/preparation.html

(require 'flycheck)
(require 'flycheck-haskell)
(eval-after-load 'flycheck
  '(add-hook 'flycheck-mode-hook #'flycheck-haskell-setup))
(add-hook 'haskell-mode-hook
	  '(lambda ()
	     (ghc-init)
             (setq flycheck-checker 'haskell-ghc)
;             (setq flycheck-checker 'haskell-hlint)
;             (setq flycheck-disabled-checkers '(haskell-ghc))
             (setq flycheck-disabled-checkers '(haskell-hlint))
	     (flycheck-mode 1)
	     (turn-on-haskell-indent)))



; enable major mode for every setting files.
;   http://rubikitch.com/2014/08/03/
(require 'generic-x)

; migemo.el for i-search kana/kanji
; http://rubikitch.com/2014/08/20/migemo/
; 
(require 'migemo)
(setq migemo-command "cmigemo")
(setq migemo-options '("-q" "--emacs"))
;; Set your installed path
(setq migemo-dictionary "/usr/local/share/migemo/euc-jp/migemo-dict") ; macではutf8はNG?
(setq migemo-user-dictionary nil)
(setq migemo-regex-dictionary nil)
(setq migemo-coding-system 'euc-jp) ; macではutf8はNG?
(load-library "migemo")
(migemo-init)

; shell-script mode 
(add-hook 'sh-mode-hook
	  '(lambda()
	     (set-variable (quote tab-width) 4)
	     (set-variable (quote electric-indent-mode) nil nil)
	     ))

;;; for emacsclient ;;;
(require 'server)
(defun server-ensure-safe-dir (dir) "Noop" t) ; avoid freeze in gnupack
(setq server-socket-dir "~/.emacs.d")
(unless (server-running-p)
  (server-start))

;;; gtags ;;;
(require 'gtags)
(add-hook 'java-mode-hook (lambda () (gtags-mode 1)))
(add-hook 'c-mode-hook (lambda () (gtags-mode 1)))
(add-hook 'c++-mode-hook (lambda () (gtags-mode 1)))
(setq gtags-mode-hook
      '(lambda ()
;         (local-set-key "\M-." 'gtags-find-tag)
;         (local-set-key "\M-." 'gtags-find-tag-from-here)
;         (local-set-key "\M-," 'gtags-find-rtag)
;         (local-set-key "\M-]" 'gtags-find-symbol)
;         (local-set-key "\M-[" 'gtags-find-file)
         (local-set-key "\C-j\C-t" 'gtags-find-tag)
         (local-set-key "\C-j\C-h" 'gtags-find-tag-from-here)
         (local-set-key "\C-j\C-p" 'gtags-find-pattern)
         (local-set-key "\C-j\C-r" 'gtags-find-rtag)
         (local-set-key "\C-j\C-s" 'gtags-find-symbol)
         (local-set-key "\C-j\C-f" 'gtags-find-file)
         (local-set-key "\C-j\C-l" 'gtags-parse-file)
         (local-set-key "\C-j\C-j" 'gtags-pop-stack)
         ))
(setq gtags-select-mode-hook
      '(lambda ()
	 (local-set-key "\C-j\C-j" 'gtags-pop-stack)
	 (local-set-key [127] 'gtags-pop-stack)      ; [DEL]
	 ))
