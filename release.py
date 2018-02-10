# -*- coding:utf-8 -*-
from funclib import T
import os
import platform
import time

def do_release():
    T.clear()
    tmp_files = ['build', 'dist', 'funclib.egg-info']
    
    T.log('Release Starting !!! ...')
    
    print('\nDeleting temporary files !!! ...\n')
    if platform.system() == "Windows":
        for f in tmp_files:
            if os.path.exists(f):
                if os.path.isfile(f):
                    os.system('del ' + f)
                else:
                    os.system('rd /s /q ' + f)
    else:
        for f in tmp_files:
            os.system('rm -rf ' + f)
    time.sleep(1)
    print('\nDelete temporary files Success!')
    
    print('\nRename README.md to README.rst !!! ...\n')
    if platform.system() == "Windows":
        os.system('ren README.md README.rst')
    else:
        os.system('mv README.md README.rst')
    time.sleep(1)
    print('\nRename README.md to README.rst Success!')
    
    print('\nBuilding Dist !!! ...\n')
    os.system('python setup.py sdist build')
    time.sleep(1)
    print('\nBuild Dist Success!')
    
    print('\nRelease !!! ...\n')
    os.system('twine upload dist/*')
    time.sleep(1)
    print('\nRelease Success!')
    
    print('\nRename README.rst to README.md !!! ...\n')
    if platform.system() == "Windows":
        os.system('ren README.rst README.md')
    else:
        os.system('mv README.rst README.md')
    time.sleep(1)
    print('\nRename README.rst to README.md Success!\n')
    
    T.log('Congratulations, Release totaly Success!')


if __name__ == '__main__':
    do_release()
