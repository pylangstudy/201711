import argparse
parser = argparse.ArgumentParser()
parser.add_argument('foo', type=int)
parser.add_argument('bar', type=open)
parser.parse_args('2 temp.txt'.split())

parser = argparse.ArgumentParser()
parser.add_argument('bar', type=argparse.FileType('w'))
parser.parse_args(['out.txt'])

import math
def perfect_square(string):
    value = int(string)
    sqrt = math.sqrt(value)
    if sqrt != int(sqrt):
        msg = "%r is not a perfect square" % string
        raise argparse.ArgumentTypeError(msg)
    return value
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=perfect_square)
parser.parse_args(['9'])
parser.parse_args(['7'])

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=int, choices=range(5, 10))
parser.parse_args(['7'])
parser.parse_args(['11'])

