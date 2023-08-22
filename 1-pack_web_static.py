#!/usr/bin/python3
""" 1. Compress before sending """

from os import mkdir
from fabric.api import local
from datetime import datetime


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
