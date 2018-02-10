# -*- coding:utf-8 -*-
from funclib import T
import os
import platform
import time

def do_release():
    T.clear()
    tmp_files = ['build', 'dist', 'funclib.egg-info']
    
    T.log('Release Starting ...')
    
    print('Deleting temporary files...')
    if platform.system() == "Windows":
        for file in tmp_files:
            if os.path.exists(file):
                if os.path.isfile(file):
                    os.system('del ' + file)
                else:
                    os.system('rd /s /q ' + file)
    else:
        for file in tmp_files:
            os.system('rm -rf ' + file)
    time.sleep(1)
    print('Delete temporary files Success!')
    
    print('Rename README.md to README.rst...')
    if platform.system() == "Windows":
        os.system('ren README.md README.rst')
    else:
        os.system('mv README.md README.rst')
    time.sleep(1)
    print('Rename README.md to README.rst Success!')
    
    print('Building Dist...')
    os.system('python setup.py sdist build')
    time.sleep(1)
    print('Build Dist Success!')
    
    print('Release...')
    os.system('twine upload dist/*')
    time.sleep(1)
    print('Release Success!')
    
    print('Rename README.rst to README.md...')
    if platform.system() == "Windows":
        os.system('ren README.rst README.md')
    else:
        os.system('mv README.rst README.md')
    time.sleep(1)
    print('Rename README.rst to README.md Success!')
    
    T.log('Congratulations, Release totaly Success!')
    
if __name__ == '__main__':
    do_release()
