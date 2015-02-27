from __future__ import print_function
from fabric.api import run, env, task, roles, local, lcd


import os
import shutil
import yaml


script_dir = os.path.dirname(__file__)

def get_selenium_root():
    return os.path.normpath(
        os.path.join(script_dir, '..', 'docker', 'selenium'))


@task
def grid_start():
    ''' start hub & node '''
    with lcd(get_selenium_root()):
        local('sudo fig up -d hub node')
        local('sudo fig ps node')


@task
def grid_stop():
    ''' stop hub & node '''
    with lcd(get_selenium_root()):
        local('sudo fig stop hub node')


@task
def selenium_start():
    ''' start selenium standalone '''
    with lcd(get_selenium_root()):
        local('sudo fig up -d selenium')


@task
def selenium_stop():
    ''' stop hub & node '''
    with lcd(get_selenium_root()):
        local('sudo fig stop selenium')


@task
def status():
    ''' stop hub & node '''
    with lcd(get_selenium_root()):
        local('sudo fig ps')


@task
def run_test():
    ''' set up ssh config file '''
    local('python selenium_test.py')
