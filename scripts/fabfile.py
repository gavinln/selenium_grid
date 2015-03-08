from __future__ import print_function
from fabric.api import run, env, task, roles, local, lcd


import os
import shutil


script_dir = os.path.dirname(__file__)


def get_jenkins_root():
    return os.path.normpath(
        os.path.join(script_dir, '..', 'docker', 'jenkins'))


def get_nodejs_root():
    return os.path.normpath(
        os.path.join(script_dir, '..', 'docker', 'nodejs'))


@task
def jenkins_start():
    ''' start jenkins master '''
    with lcd(get_jenkins_root()):
        local('sudo fig up -d ciserver')
        local('sudo fig ps ciserver')


@task
def jenkins_stop():
    ''' stop jenkins master '''
    with lcd(get_jenkins_root()):
        local('sudo fig stop ciserver')


@task
def nodejs_start():
    ''' start nodejs jenkins slave '''
    with lcd(get_nodejs_root()):
        local('sudo fig up -d cislave')


@task
def nodejs_stop():
    ''' stop nodejs jenkins slave '''
    with lcd(get_nodejs_root()):
        local('sudo fig stop cislave')


@task
def status():
    ''' stop hub & node '''
    with lcd(get_jenkins_root()):
        local('sudo fig ps')
    with lcd(get_nodejs_root()):
        local('sudo fig ps')
