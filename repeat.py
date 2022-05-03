import sys

l=sys.argv[1:]

if len(l)==1 or len(l)==0:
    try:
      n=int(l[0])
    except ValueError as e:
        print("alert\n")
        print("msg : ",e.args[0])
        #print("msg : ",e.msg)
        exit(2)
    if len(l)==0 or n<0:
        n=5
    print("\n\nn is : --> ",n)
    print()
    print('-'*n)
    print('End of Code...')
    print()
else:
    print("\n\tToo Many Arguments...")
    exit(1)

