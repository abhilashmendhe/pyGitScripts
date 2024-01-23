import os, sys, pygit2
from pygit2 import discover_repository
from pygit2.repository import Repository,Signature
from pygit2.refspec import Refspec
path = os.path.abspath("./")

args = sys.argv

if len(args) < 2:
    print("Please specify the origin")
    os._exit(1)

origin = args[1]

inGitRepo = discover_repository(path)

if not inGitRepo:
    print("Please be inside a git repo.")
    os._exit(1)

repo = Repository(path)

try:
    remote = repo.remotes[origin]
    tp = remote.fetch()
    print("indexed_deltas: ",tp.indexed_deltas)
    print("index_objects: ",tp.indexed_objects)
    print("local_objects: ",tp.local_objects)
    print("received_bytes: ",tp.received_bytes)
    print("received_objects: ", tp.received_objects)
    print("total_deltas: ",tp.total_deltas)
    print("total_objects: ",tp.total_objects)
    
except Exception as e:
    print(e)
    print(f"remote {origin} does not exists!")  

