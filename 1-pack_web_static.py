#!/usr/bin/python3
'''script to generate tgz archive'''
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    '''to compress files'''
    if not os.path.isdir('versions'):
        if local('mkdir -p versions').failed is True:
            return None
    dn = datetime.utcnow()
    arc = "versions/web_static_{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz"\
           .format(dn.year, dn.month, dn.day, dn.hour, dn.minute, dn.second)
    if local('tar -cavf {} web_static'.format(arc)).failed is True:
        return None

    return arc
