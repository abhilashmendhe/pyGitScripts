from pygit2.repository import Repository
from pygit2 import discover_repository, Signature
import pygit2, os, sys

path = os.path.abspath("./")
print(path)

args = sys.argv

if len(args) < 2:
    print("Please specify the process name!")
    os._exit(1)

p_name = args[1]


git_path = os.path.abspath("./") + "/" + p_name

# Check if git repo exists. discovery_respository checks for .git folder also
isPresent = discover_repository(git_path)

if isPresent:
    print(p_name+" git repo already exists!")
    os._exit(1)

# Git init
ans = pygit2.init_repository(git_path, False)

# Create a repository object. Create a TreeBuilder to write a tree.
repo = Repository(git_path)
tree = repo.TreeBuilder().write()

print("Repo inititialization sucessful!")

# Change directory
os.chdir(git_path)

# Creating a branch
isBranch = repo.branches.get(p_name)

if isBranch:
    print(f"Branch {p_name} already exists!")
    os._exit(1)


email = f"{p_name}@email.com"
msg = f"Author '{p_name}' initialized. process-init"
author   = Signature(p_name, email)
commiiter = Signature(p_name, email)
refsHeads = f"refs/heads/{p_name}"

firstHash = repo.create_commit(refsHeads, 
                   author, 
                   commiiter, 
                   msg,
                   tree, 
                   [])
# Create a git-cb file and add the dir. name
git_cb_path = git_path + "/.git/git-cb"
with open(git_cb_path, "a") as f:
    f.write(p_name+"\n")
    f.write(str(firstHash))
    f.close()
    
newmsg = msg+" in repo "+path
print(p_name)
print(firstHash)
print(newmsg)