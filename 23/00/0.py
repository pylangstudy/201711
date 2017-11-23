import getopt
args = '-a -b -cfoo -d bar a1 a2'.split()
print(args)
optlist, args = getopt.getopt(args, 'abc:d:')
print(optlist)
print(args)

