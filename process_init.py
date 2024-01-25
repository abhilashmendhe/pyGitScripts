from pygit2.repository import Repository
from pygit2 import discover_repository, Signature
import os
import sys
from subprocess import call

path = os.path.abspath("./")
print(path)

args = sys.argv

if len(args) < 2:
    print("Please specify the process name!")
    os._exit(1)

p_name = args[1]

git_path = path + "/" + p_name
call(["python3", path+"/pyGitScripts/repo_init.py",p_name])
os.chdir(git_path)
call(["python3",path+"/pyGitScripts/author_init.py",p_name,"process-init"])