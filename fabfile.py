#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, run, env, cd, hosts
from fabric.context_managers import settings

CODE_DIR = "/var/www/sites/deploytest"

env.hosts = ['192.168.1.24:22']
env.user = "megane"


@hosts('localhost')
def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -m \" %s \"" % message)
    local("git push github master")


@hosts('192.168.1.24:22')
def pull():
    with cd(CODE_DIR):
        run("git pull origin master")
        #再読み込み
        with settings(warn_only=True):
            run("gaffer unload")
        run("gaffer load")


def deploy():
    commit()
    pull()
