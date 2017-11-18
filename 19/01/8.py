import argparse
import textwrap
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('--foo')
parser.add_argument('bar', nargs='?')
print(parser.parse_args(['--foo', '1', 'BAR']))
print(parser.parse_args([]))
