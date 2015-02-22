from __future__ import print_function
from fabric.api import run, env, task, roles, local, lcd


import os
import shutil
import yaml


script_dir = os.path.dirname(__file__)


@task
def start_node():
    ''' start node '''
    selenium_root = os.path.normpath(
        os.path.join(script_dir, '..', 'docker', 'selenium'))
    with lcd(selenium_root):
        local('sudo fig up -d')


@task
def stop_node():
    ''' stop node '''
    selenium_root = os.path.normpath(
        os.path.join(script_dir, '..', 'docker', 'selenium'))
    with lcd(selenium_root):
        local('sudo fig stop')


@task
def run_test():
    ''' set up ssh config file '''
    local('python selenium_test.py')
