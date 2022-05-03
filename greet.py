import sys
from getopt import *

l=sys.argv

if len(l)<=1:
    print("Anonymous User Welcome to my Pc...")
elif len(l)>4:
    print("to Many arguments are given Please take care of it...")
else:
    name=' '.join(sys.argv[1:])
    print("Hello ,",name,"--> Welcome To My World ...")
    exit(3)
