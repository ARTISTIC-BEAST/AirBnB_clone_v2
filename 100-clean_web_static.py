#!/usr/bin/python3
""" 4. Keep it clean! """

from fabric.api import local, run, env
from fabric.context_managers import cd, lcd
from fabric.operations import put
from datetime import datetime


env.hosts = ['web-01.wisvem.tech', 'web-02.wisvem.tech']
# env.hosts = ['e98e448bd522@7e5652f1.hbtn-cod.io:22']
# env.passwords = {'e98e448bd522@7e5652f1.hbtn-cod.io:22':\
#  'f372b89afe065fa3d645'}


def do_pack():
    """Do pack """
    path = None
    try:
        local("mkdir -p versions")
        x = datetime.now()
        date = x.strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static/".format(path))
    except:
        pass
    return path


def do_deploy(archive_path):
    """Do deploy"""
    if archive_path is None:
        return False
    try:
        fn = "{}".format(archive_path.split('/')[1])
        # File name withou extension
        fn_nex = fn.split('.')[0]
        with cd('/tmp'):
            put(archive_path, fn)
        run("mkdir -p /data/web_static/releases/{}".format(fn_nex))
        r_path = "/data/web_static/releases/{}".format(fn_nex)
        run("tar -xzf /tmp/{} -C {}".format(fn, r_path))
        run("rm /tmp/{}".format(fn))
        r_p2 = "/data/web_static/releases/"
        run("mv {}{}/web_static/* {}/".format(r_p2, fn_nex, r_path))
        run("rm -rf {}/web_static".format(r_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(r_path))

        return True
    except:
        return False


def deploy():
    """ Deploy """
    return do_deploy(do_pack())


def do_clean(number=0):
    """ Do clean """
    try:
        number = int(number)
    except:
        return None
    if number < 0:
        return None
    if (number is 0 or number is 1):
        number = 2
    else:
        number += 1
    r_path = "/data/web_static/releases/"
    l_path = "./versions"
    with lcd(l_path):
        local('ls -t | tail -n +{} | xargs rm -rf --'.
              format(number))
    with cd(r_path):
        run('ls -t | tail -n +{} | xargs rm -rf --'.
            format(number))
