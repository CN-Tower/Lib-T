import sys

if sys.version[0] != '2':
    from funclib.funclib import FuncLib as fn
else:
    from .funclib import FuncLib as fn
