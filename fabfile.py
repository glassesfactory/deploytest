#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, run, env, cd, hosts

CODE_DIR = "/var/www/sites/"
env.host = ['192.168.1.24']
env.user = "megane"
# env.password = ''

# @hosts('localhost:5959')
def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -m \" %s \"" % message)
    local("git push github master")


# @hosts('49.212.197.36:10022')
def pull():
    with cd(CODE_DIR):
        run("git pull origin master")
        #再読み込み
        with cd("blog"):
            run("gaffer unload")
            run("gaffer load")


def deploy():
    commit()
    pull()
