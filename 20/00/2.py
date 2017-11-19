import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs=2)
parser.add_argument('bar', nargs=1)
parser.parse_args('c --foo a b'.split())

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('bar', nargs='?', default='d')
parser.parse_args(['XX', '--foo', 'YY'])
parser.parse_args(['XX', '--foo'])
parser.parse_args([])

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
parser.parse_args(['input.txt', 'output.txt'])
parser.parse_args([])

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*')
parser.add_argument('--bar', nargs='*')
parser.add_argument('baz', nargs='*')
parser.parse_args('a b --foo x y --bar 1 2'.split())

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', nargs='+')
parser.parse_args(['a', 'b'])
parser.parse_args([])

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo')
parser.add_argument('command')
parser.add_argument('args', nargs=argparse.REMAINDER)
print(parser.parse_args('--foo B cmd --arg1 XX ZZ'.split()))


