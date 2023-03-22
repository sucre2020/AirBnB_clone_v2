#!/usr/bin/python3
"""Full deploy module"""

from fabric.api import *
from os.path import exists, isdir
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['35.227.111.39', '3.84.128.123']


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


def do_deploy(archive_path):
    """Deploys the web page in the tar archive"""
    if not exists(archive_path) or (exists(archive_path) and
                                    isdir(archive_path)):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[1]
        dir_name = file_name.split('.')[0]
        command_dir = 'mkdir -p /data/web_static/releases/{}'.format(dir_name)
        run(command_dir)
        command_ext = 'tar -xzf /tmp/{}'.format(file_name)
        command_ext += ' -C /data/web_static/releases/{}'.format(dir_name)
        run(command_ext)
        command_rm = 'rm /tmp/{}'.format(file_name)
        run(command_rm)
        command_mv = 'mv /data/web_static/releases/'
        command_mv += '{}/web_static/*'.format(dir_name)
        command_mv += ' /data/web_static/releases/{}/'.format(dir_name)
        run(command_mv)
        command_rd = 'rm -rf /data/web_static/releases/{}'.format(dir_name)
        command_rd += '/web_static'
        run(command_rd)
        run('rm -rf /data/web_static/current')
        command_ln = 'ln -s /data/web_static/releases/{}/'.format(dir_name)
        command_ln += ' /data/web_static/current'
        run(command_ln)
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Deploys the full website using do_pack and do_deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    depoyment_status = do_deploy(archive_path)
    return deployment_status
