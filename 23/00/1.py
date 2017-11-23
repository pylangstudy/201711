import getopt
s = '--condition=foo --testing --output-file abc.def -x a1 a2'
args = s.split()
print(args)
optlist, args = getopt.getopt(args, 'x', ['condition=', 'output-file=', 'testing'])
print(optlist)
print(args)

