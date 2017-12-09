#!/usr/bin/env bash

git_username=${1:-"David Garcia-Campos"}
git_email=${2:-"dgarciacampos@gmail.com"}

if [ "$#" -ne 2 ]; then
    echo "$0 git_username git_email"
    printf "\tExample:\n\t$0 ${git_username} ${git_email}\n"
fi
# TODO: validate ARG1 and ARG2

# TODO: check if ~/.gitconfig has user.name/user.email define

git config --global user.name "${git_username}"
git config --global user.email "${git_email}"