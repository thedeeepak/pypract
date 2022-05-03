import sys
from getopt import *

try:
  opts , args = getopt(sys.argv[1:],"nc:h:",("align="))
except GetoptError as e:
    print("\nalert\n")
    print("msg : ",e.msg)
    print("opt : ",e.opt)
    exit(1)

print()
#print("Note : please Do not use * , | , ( , ) , & in opt -c") Bcz these operators are used by Linux
#print()
optdict={}
argdict={}

for t in opts:
    if t[0]=='--align':
      val=t[1].upper()
    else:
      val=t[1]
    optdict[t[0]]=val

if '-c' not in optdict:
    optdict['-c']='*'
elif len(optdict['-c'])>1:
    optdict['-c']='*'
if '-h' not in optdict:
    optdict['-h']=10
elif '-h' in optdict:
    try:
      h=int(optdict['-h'])
    except ValueError as e:
      print("msg : ",e.args[0])
      exit(2)
h=int(optdict['-h'])

if int(optdict['-h'])<0:
    h=10
c=optdict['-c']
if '--align' not in optdict:
    optdict['--align']='CENTER'

if "-n" in optdict:
#left
  if "LEFT" in optdict['--align']:
     print('\n'.join(map(lambda i:f"{i:>2} "+f"{c*i}",range(1,h+1))))
     print()
#Right
  elif "RIGHT" in optdict['--align']:
    print('\n'.join(map(lambda i:f"{i:>2} "+f"{c*i:>{h}}",range(1,h+1))))
    print()
  ##Center
  elif "CENTER" in optdict['--align']:
    print('\n'.join(map(lambda i:f"{i:>2}"+f"{c*(2*i-1):^{2*h+4}}",range(1,h+1))))
    print()
  else:
      print("Please Enter Valid Option in align ...")
      exit(2)
#Without Number
else:
#Center
#left
  if "LEFT" in optdict['--align']:
    print('\n'.join(map(lambda i:f"{c*i}",range(1,h+1))))
    print()
#Right
  elif "RIGHT" in optdict['--align']:
    print('\n'.join(map(lambda i:f"{c*i:>{h}}",range(1,h+1))))
    print()
#center
  elif "CENTER" in optdict['--align']:
    print('\n'.join(map(lambda i:f"{c*(2*i-1):^{2*h+4}}",range(1,h+1))))
    print()

print("<-- -----------------------------Exit-------------------------------- -->")






