;; set home dir
(setq local-home-dir "/cygwin/home/kurokawa/")

;; set font size & screen size for 4K
(set-face-attribute 'default nil :height 240)
(setq default-frame-alist
  '(
    (width . 80)
    (height . 50)
   )
)

;; path for ghc related elisp files
(setq local-ghcmod-dir "~/AppData/Roaming/cabal/x86_64-windows-ghc-7.10.2/ghc-mod-5.5.0.0/elisp/")
(setq local-hlint-dir "~/AppData/Roaming/cabal/x86_64-windows-ghc-7.10.2/hlint-1.9.30/")
