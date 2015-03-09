from __future__ import print_function
from fabric.api import run, env, task, roles, local, lcd


import os
import shutil


script_dir = os.path.dirname(__file__)


def get_docker_path(dockerDir):
    return os.path.normpath(
        os.path.join(script_dir, '..', 'docker', dockerDir))


def get_jenkins_root():
    return get_docker_path('jenkins')


def get_nodejs_root():
    return get_docker_path('nodejs')


def get_selenium_root():
    return get_docker_path('selenium')


def get_python_root():
    return os.path.normpath(
        os.path.join(script_dir, '..', 'python'))


@task
def jk_master_start():
    ''' start jenkins master '''
    with lcd(get_jenkins_root()):
        local('sudo fig up -d ciserver')
        local('sudo fig ps ciserver')


@task
def jk_master_stop():
    ''' stop jenkins master '''
    with lcd(get_jenkins_root()):
        local('sudo fig stop ciserver')


@task
def jk_slave_start():
    ''' start jenkins nodejs slave '''
    with lcd(get_nodejs_root()):
        local('sudo fig up -d cislave')


@task
def jk_slave_stop():
    ''' stop jenkins nodejs slave '''
    with lcd(get_nodejs_root()):
        local('sudo fig stop cislave')


@task
def jk_status():
    ''' status of jenkins master & slave '''
    with lcd(get_jenkins_root()):
        local('sudo fig ps')
    with lcd(get_nodejs_root()):
        local('sudo fig ps')


@task
def sl_grid_start():
    ''' start selenium hub & node '''
    with lcd(get_selenium_root()):
        local('sudo fig up -d hub node')
        local('sudo fig ps node')


@task
def sl_grid_stop():
    ''' stop selenium hub & node '''
    with lcd(get_selenium_root()):
        local('sudo fig stop hub node')


@task
def sl_standalone_start():
    ''' start selenium standalone '''
    with lcd(get_selenium_root()):
        local('sudo fig up -d standalone')


@task
def sl_standalone_stop():
    ''' stop selenium standalone '''
    with lcd(get_selenium_root()):
        local('sudo fig stop standalone')


@task
def run_test():
    ''' run python test scripts '''
    with lcd(get_python_root()):
    	local('python selenium_test.py')
