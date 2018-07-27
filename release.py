#!/usr/bin/env python
# -*- coding:utf-8 -*-
from funclib import fn
import os
import shutil
import platform
import time

def del_temp_files():
    print('\nDeleting temp files !!! ...\n')
    tmp_files = ['build', 'dist', 'funclib.egg-info', 'README.rst']
    for f in tmp_files:
        if os.path.exists(f):
            if os.path.isfile(f):
                os.remove(f)
            else:
                shutil.rmtree(f) 
    time.sleep(1)
    print('\nDelete temp files Success!')

def cp_md_2_rst():
    print('\nCoping README.md to README.rst !!! ...\n')
    shutil.copyfile("README.md","./README.rst") 
    time.sleep(1)
    print('\nCoping README.md to README.rst Success !!! ...\n')


def build_dist(): 
    print('\nBuilding Dist !!! ...\n')
    os.system('python setup.py sdist build')
    time.sleep(1)
    print('\nBuild Dist Success!')

def release_funclib():
    print('\nRelease !!! ...\n')
    status_code = os.system('twine upload dist/*')
    if status_code != 0:
        raise Exception('Release Error, Please make sure you have installed the "twine" module already!')
    time.sleep(1)
    print('\nRelease Success!')

if __name__ == '__main__':
    fn.clear()
    fn.log('Release Starting !!! ...')
    del_temp_files()
    cp_md_2_rst()
    build_dist()
    release_funclib()
    fn.log('Congratulations, Release totaly Success!')
    
