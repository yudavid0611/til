# Basic commands

## Introduction
- basic commands of git.
- there are also some Linux commands.

<br/>

> **references**: https://git-scm.com/docs/git-config

<br/>

## contents

- **touch**: make a file.
    - working directory: a.txt
    - subdirectory: folder/a.txt
- **mkdir**: make a folder .
    - mkdir git-practice
- **ls**(list segment): display folders and files in the current directory.
    - **ls -a**
        - ./: current directory
        - ../: parent directory
- **cd**(change directory): change the current directory into a new directory.
- **rm**(remove): delete a file.
    - rm a.txt
- **git init**: Make a local repository.
- **git status**: display the state of the working directory and the staging area.
- **git add {file name}**: add new files or modified files in the working directory to the staging area.
    - **git add .**: apply it to all of the files in the working directory.
- **code .** : execute VSCode
- **git config --global {user.email} {user's email}**: set user's email.
- **git config --global {user.name} {user's name}**: set user's name.
- **git commit -m ‘{message}’**: commit with a message. There is not any specific regulation about writing a message. But generally, it contains the reason why a new version was committed.
- **git log**: display the history of commits in the repository.
    - **git log --oneline**: display it briefly.
- **clear**:(=control+l): clear the terminal.
- **git remote add origin {remote repo url}**: add the remote repository to the local repository with the name 'origin.'
- **git push origin master**: upload the local repository contents to the remote repository.
    - **git push -u origin master**: after using this command, you can upload by using just the '**git push**' command.
- **git pull origin master**: update a repository.
- **git clone {repository url}**: download a remote repository.
- **git config --list**: list all variables set in config file, along with their values.
- **git restore --staged {tracked file}**: move a tracked file from the staging area to the working directory. 
- **git mv {former file name} {new file name}**: rename a file.