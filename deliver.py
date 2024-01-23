from pygit2.repository import Repository
from pygit2 import discover_repository, Signature
import os, time, sys
from subprocess import call

args = sys.argv
interval = None

if len(args) >= 2:
    interval = args[1]

path = os.path.abspath("./")
ind = path.rfind("/")
push_path = path[:ind]

isValid = discover_repository(path)

if not isValid:
    print("Please be inside a git repo, to deliver the message")
    os._exit(1)

call(["python3", push_path+"/pyGitScripts/repo_merge.py"])
if interval:
    time.sleep(int(interval))
    call(["python3", push_path+"/pyGitScripts/repo_deliver.py"])
