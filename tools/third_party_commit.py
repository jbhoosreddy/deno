#!/usr/bin/env python
# This script generates the third party dependencies of deno.
# - Get Depot Tools and make sure it's in your path.
#   http://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up
# - You need yarn installed as well.
#   https://yarnpkg.com/lang/en/docs/install/
# Use //gclient_config.py to modify the git deps.
# Use //js/package.json to modify the npm deps.

import os
from os.path import join
import subprocess
from util import run, remove_and_symlink
import shutil

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
third_party_path = join(root_path, "third_party")

try:
    os.makedirs(third_party_path)
except:
    pass
os.chdir(third_party_path)
gitdirs = subprocess.check_output("find . | egrep .git$", shell=True).strip().split("\n")
for gd in gitdirs:
    if gd == "./.git" or gd == ".git":
        continue
    repo_git_dir = os.path.join(third_party_path, gd)
    repo = os.path.dirname(repo_git_dir)
    os.chdir(repo)
    sha = subprocess.check_output("git rev-list HEAD -1", shell=True).strip()
    # TODO Sanity check sha against those stored in gclient_config.py.
    print sha, repo
    print "rm -rf " + repo_git_dir
    shutil.rmtree(repo_git_dir) # Delete the .git directories.

os.chdir(third_party_path)
