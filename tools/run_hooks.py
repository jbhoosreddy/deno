#!/usr/bin/env python
import os
import sys
from util import run

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
third_party_path = os.path.join(root_path, "third_party")
depot_tools_path = os.path.join(third_party_path, "depot_tools")
os.chdir(third_party_path)


def download(fn):
    run([ os.path.join(depot_tools_path + '/download_from_google_storage.py'),
        '--no_resume',
        '--platform=' + sys.platform, '--no_auth', '--bucket', 'chromium-gn', '-s',
        os.path.join(third_party_path, fn) ])


run(['python', 'v8/tools/clang/scripts/update.py'])

if sys.platform == 'win32':
    download("v8/buildtools/win/gn.exe.sha1")
elif sys.platform == 'darwin':
    download("v8/buildtools/mac/gn.sha1")
elif sys.platform.startswith('linux'):
    download("v8/buildtools/linux64/gn.sha1")
