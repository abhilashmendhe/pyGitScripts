import pygit2
from pygit2.repository import Repository
import os

inp = input("Enter directory name: ")

if inp == "":
    print("Please specify the name!")
    os._exit(1)

path = os.path.abspath("./")
dirs = os.listdir(path)

if inp in dirs:
    print(inp+" directory already exists!")
    os._exit(1)

git_path = path + "/" +inp

# Git init
ans = pygit2.init_repository(git_path, False)

# Create a git-cb file and add the dir. name
git_cb_path = git_path + "/.git/git-cb"
with open(git_cb_path, "w") as f:
    f.write(inp)
    f.close()

repo = Repository(git_path)
treeObj = repo.TreeBuilder()
tobj = treeObj.write()

print("Repo inititialization sucessful!")