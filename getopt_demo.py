import sys
from getopt import *

#print(argv)
try:
 opts , args = getopt(sys.argv[1:],'no:v:',["name","options=","verbose="])
except GetoptError as e:
 print("Usage [-n] optional Values [-o] required valued(optional) [-v] verbose  or ")
 print("Usage [--name] optional Values [--options] required valued(optional) [--verbose] verbose...")
 print()
 print("msg : ",e.msg)
 print("opt : ",e.opt)
 exit(1)
print(opts,"--> Opts")
print(args,"--> Args")

