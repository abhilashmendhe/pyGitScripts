import pygit2
from pygit2 import discover_repository
from pygit2.repository import Repository
import os, sys

args = sys.argv

if len(args) < 2:
    print("Please specify the name of repo!")
    os._exit(1)

inp = args[1]

git_path = os.path.abspath("./") + "/" + inp

# Check if git repo exists. discovery_respository checks for .git folder also
isPresent = discover_repository(git_path)

if isPresent:
    print(inp+" git repo already exists!")
    os._exit(1)

# Git init
ans = pygit2.init_repository(git_path, False)

# Create a git-cb file and add the dir. name
git_cb_path = git_path + "/.git/git-cb"
with open(git_cb_path, "w") as f:
    f.write(inp)
    f.close()

# Create a repository object. Create a TreeBuilder to write a tree.
repo = Repository(git_path)
treeObj = repo.TreeBuilder()
tobj = treeObj.write()

print("Repo inititialization sucessful!")