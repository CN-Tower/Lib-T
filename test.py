import os

def test_funclib():
    os.system('coverage run test/funclib.test.py')
    os.system('coverage report -m')

if __name__=='__main__':
    test_funclib()
