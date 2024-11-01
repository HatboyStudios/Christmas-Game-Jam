# Christmas-Game-Jam
Gather some programmers, and non programmers to program a game over our collective christmas breaks


## Prerequisites
- Python (latest version)
- Visual Studio Code (or any code editor)
- Git

## Clone the Repository
```git clone https://github.com/HatboyStudios/Christmas-Game-Jam.git```

## Creating Python Virtual Environment
Open the Project folder in your code editior and terminal and enter the following command
```python3 -m  venv .venv```

## Running Python Virtual Environment
Run the following command based on your operating system
### MacOs/Linux
```. .venv/bin/activate```

### Windows
```.venv\Scripts\activate```

## Run the Program
Enter the command in your terminal ```python3 main.py```

# Github Information
## Creating a new Branch
When developing within a group, or large scale project; it's good to create branches to test the new code you want to add to the program without causing errors or major bugs to the main branch

```git checkout -b [Branch Name]```

## Switching Branches
```git checkout [Branch Name]```

## Commit Code
when committing you enter the first command to add the files to the git repo, and run the second command to save everything to your local repository, each commit you make saves on whatever current branch you're on.
```
git add --all
git commit -a -m "[Commit Message]"
```

## Pushing Code
after committing, you will need to push your code to the global repository, so the other developers can pull your code down to their own local repository
```
git push
```

## Pulling Code
for when you need to pull code from the global repo to your local repo. Good practice to pull code every time before you start working to check for any updates on a branch.
```
git pull
```
