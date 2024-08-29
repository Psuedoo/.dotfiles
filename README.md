# Psuedoo's Dotfiles

I am using [this link](https://www.anand-iyer.com/blog/2018/a-simpler-way-to-manage-your-dotfiles/) to setup/manage my dotfiles.
## Setting Up a New Machine

To set up a new machine to use your version controlled config files, all you need to do is to clone the repository on your new machine telling git that it is a bare repository:

```bash
git clone --separate-git-dir=$HOME/.dotfiles git@github.com:Psuedoo/.dotfiles.git ~
```

However, some programs create default config files, so this might fail if git finds an existing config file in your $HOME. In that case, a simple solution is to clone to a temporary directory, and then delete it once you are done:

```bash
git clone --separate-git-dir=$HOME/.dotfiles git@github.com:Psuedoo/.dotfiles.git tmpdotfiles
rsync --recursive --verbose --exclude '.git' tmpdotfiles/ $HOME/
rm -r tmpdotfiles
```

There you go. No symlink mess.




I am using [kickstart.nvim](https://github.com/psuedoo/kickstart.nvim) for my starting Neovim config.
