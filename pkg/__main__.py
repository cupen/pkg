# coding:utf-8
"""A simple wrapper of package manager.

Usage:
    pkg search PKGNAME...
    pkg show PKGNAME...
    pkg install PKGNAME...
    pkg uninstall PKGNAME...
    pkg depends PKGNAME...
    pkg list
    pkg update
    pkg upgrade
Arguments:
    PKGNAME     package name.
Options:
  -h --help     Show this infomation.
  --version     Show version.
  --debug       Show debug infomation.
"""
VERSION = "0.0.1"

import os
from docopt import docopt
from pkg.distroconf import get_distro_command


def main(**kwargs):
    cmd_inputed = list(filter(lambda cmd: isinstance(kwargs[cmd],bool) and kwargs[cmd], kwargs.keys()))
    if len(cmd_inputed) != 1:
        print("Invalid params.")
        exit(1)

    cmd_tmpla = get_distro_command(cmd_inputed[0])
    if not cmd_tmpla:
        exit(2)

    final_inputed = cmd_tmpla if cmd_tmpla.find('%s') == -1 else cmd_tmpla%(' '.join(kwargs['PKGNAME']),)
    print(">>> " + final_inputed)
    os.system(final_inputed)
    pass

def main_too():
    args = docopt(__doc__, version=VERSION)
    main(**args)
    pass


if __name__ == '__main__':
    main_too()
    pass
