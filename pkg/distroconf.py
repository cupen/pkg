# coding:utf-8
import platform
import traceback

__author__ = 'cupen'

CMD_WRPPER_DICT = {}
CMD_WRPPER_DICT['Ubuntu'] = {
    "search":    'apt-cache search %s',
    "install":   'apt-get install %s',
    "uninstall": 'apt-get autoremove --purge %s',
    "list":      'dpkg -l',
    "show":      'apt-cache show %s',
    "depends":   'apt-cache depends %s',
    "update":    'apt-get update',
    "upgrade":   'apt-get upgrade',
}

CMD_WRPPER_DICT['Archlinux'] = {
    "search":    'pacman -Ss %s',
    "install":    'pacman -S %s',
    "upgrade":   'pacman -Syyu',
}

def get_distro_name():
    uname_result = platform.uname()
    if uname_result.system not in ('Linux',):
        print("It must be a linux distro")
        return None

    distname, distversion, distid = platform.dist()
    return distname

def get_distro_command(cmd, distro_name = None):
    global CMD_WRPPER_DICT
    distro_name = get_distro_name()
    if distro_name not in CMD_WRPPER_DICT:
        raise Exception("Unsupports distro '%s'"%(distro_name,))

    _dict = CMD_WRPPER_DICT[distro_name]
    if cmd not in _dict:
        raise Exception("Unsupports cmd '%s' for distro '%s'"%(cmd, distro_name,))

    return _dict[cmd]
