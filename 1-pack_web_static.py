#!/usr/bin/python3
"""Module that packs files to be passed to a server using tar"""

from fabric.api import *
from os.path import exists, isdir
from datetime import datetime


def do_pack():
    """Packs all files in the web_static directory using tar"""
    if not exists('versions') or (exists('versions') and
                                  not isdir('versions')):
        local('mkdir -p versions')
    date = datetime.now()
    command = 'tar -cvzf '
    filename = 'versions/web_static_'
    filename += '{:4}{:02}{:02}'.format(date.year, date.month, date.day)
    filename += '{:02}{:02}{:02}'.format(date.hour, date.minute, date.second)
    filename += '.tgz'
    command += filename
    command += ' web_static'
    print("Packing web_static to {}".format(filename))
    try:
        local(command)
        return filename
    except:
        return None
