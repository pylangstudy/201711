import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('bar')
parser.parse_args('X --foo Y'.split())
parser.print_help()

parser = argparse.ArgumentParser()
parser.add_argument('--foo', metavar='YYY')
parser.add_argument('bar', metavar='XXX')
parser.parse_args('X --foo Y'.split())
parser.print_help()

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x', nargs=2)
parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
parser.print_help()

