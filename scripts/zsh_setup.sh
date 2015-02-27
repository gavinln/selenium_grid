#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# setup ohmyzsh
if [ ! -d ~/.oh-my-zsh ]; then
    wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh
    chsh -s /bin/zsh
fi


# setup z.sh to help traverse directories
cp $DIR/z.sh ~/z.sh

ZSHRC=~/.zshrc
ZSH_SETUP="source ~/z.sh"

if ! grep -qe "$ZSH_SETUP" $ZSHRC; then
    echo "$ZSH_SETUP" >> $ZSHRC
fi

# setup ohmyzsh plugins
sed -i "s/plugins=(git)/plugins=(git fabric)/" $ZSHRC

