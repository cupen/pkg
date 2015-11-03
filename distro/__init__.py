# coding:utf-8
import platform
import traceback
import distro.ubuntu
import re

DEBUG = False

def get_distro():
    uname_result = platform.uname()
    if uname_result.system not in ('Linux',):
        print("It must be a linux distro")
        return None

    distname, distversion, distid = platform.dist()
    return load_pkg_manager_wrapper(distname, distversion)

def load_pkg_manager_wrapper(distname, distversion):
    try:
        return __import__('distro.' + distname.lower())
    except:
        if DEBUG: traceback.print_exc()
        pass

    return None


class DistroBase:

    def __init__(self):
        pass

    def runcmd(self, cmd):
        pass

    def install(self, pkgname, version=''):
        pass

    def uninstall(self, pkgname, version=''):
        pass

    def list(self, pkgname=''):
        pass