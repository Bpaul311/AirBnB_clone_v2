#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime


def pack():

    """
    Making an archive on a web server
    """

    time = datetime.now()

    archive = 'webstatic_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions / {} web_static'.format(archive))
    if create is None:
        return None
    else:
        return archive