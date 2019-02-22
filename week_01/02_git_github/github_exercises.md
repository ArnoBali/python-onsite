# Git and GitHub

There are two main ways in which you get started working with a
git repository on your local machine:

1. The first is to initialize a folder, or a project, as a new git repository. This creates the `.git` folder in the project that tracks all of the git functionality.
2. The second way is to clone an existing repository from GitHub onto your machine.

## Cloning repository from GitHub:
- create a new folder in your CodingNomads folder called "clone_wars"
mkdir clone_wars
- clone the following repository into "clone_wars":
[https://github.com/martin-martin/clone-test](https://github.com/martin-martin/clone-test)
cd clone_wars
git clone https://github.com/martin-martin/clone-test
- through GitHub's website, create a new repository with the same name as the repository that you cloned
https://github.com/ArnoBali/clone_wars.git
- add a new remote to your local git repository that points to the repo that you just created on your own GitHub
cd clone-test
git remote add arno https://github.com/ArnoBali/clone_wars.git
git push -u arno master
- push the local repository to your GitHub repository
git push arno
- visit the GitHub repo to make sure the contents were pushed
https://github.com/ArnoBali/clone_wars

## Initializing a new git repository:
- in your CodingNomads folder, create new folder git_practice
mkdir git_practice
- inside git_practice:
    - initialize folder as a git folder (make sure you are in the
    correct folder when initializing)
    git init
    - make new file
    touch readme.txt
    - add file
    git add readme.txt
    - commit file
    git commit -m "first commit"
    - on GitHub, create new git_practice repository
    https://github.com/ArnoBali/git_practice.git
    - add remote that points to the GitHub repository
    git remote add origin https://github.com/ArnoBali/git_practice.git
    - push committed file to GitHub
    git push -u origin master
    - practice the following git flow until you feel comfortable:
        - Create or modify file
        touch.txt
        - Add file(s)
        git add text.txt
        - Commit file(s)
        git commit -m "2nd commit"
        - Push file(s) to GitHub repository
        git push

## More practice cloning
- spend some time looking at the repositories on GitHub
- find three projects that interest you and clone them to your
local machine (in a new folder inside of CodingNomads)
- create repositories on your GitHub for each project
- add remotes to each local repo
- push each repo to your GitHub
