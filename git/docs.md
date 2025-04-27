# Git-related Documentation

This readme file entails all git-related commands, files, etc...


## Commands
```sh
# Common commands
git status
git log --oneline
git fetch
git pull
git push
```

- Reset
    - Example: `git reset <commit-hash>`, `git reset HEAD`, `git reset HEAD~n`
    ```sh
    # Reset commit, unstaged changes, keep working directory
    git reset

    # Reset commit, staged changes, keep working directory
    git reset --soft
    
    # Reset commit, delete uncommited working directory
    git reset --hard
    ```

# Git LFS
- Reference: [https://docs.github.com/en/repositories/working-with-files/managing-large-files](https://docs.github.com/en/repositories/working-with-files/managing-large-files)
- Installation
    - Install git lfs
    ```sh
    # Mac
    brew install git-lfs

    # make required changes to your global Git config
    git lfs install
    ```
- Tracking
    ```sh
    # track file
    git lfs track "*.psd"
    ```
    - Add `.gitattributes` file **before** commiting large files
- Managing
    ```sh
    git lfs pull
    git lfs prune
    ```
