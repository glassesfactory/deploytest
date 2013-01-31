#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, run, env, cd, hosts

CODE_DIR = "/var/www/sites/deploytest"

env.user = "megane"# env.password = ''


@hosts('localhost')
def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -m \" %s \"" % message)
    local("git push github master")


@hosts('192.168.1.24:22')
def pull():
    with cd(CODE_DIR):
        run("git pull github master")
        #再読み込み
        run("gaffer unload")
        run("gaffer load")


def deploy():
    commit()
    pull()
