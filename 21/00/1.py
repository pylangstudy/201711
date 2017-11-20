import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', type=int)
parser.add_argument('bar', nargs='?')

# invalid type
print(parser.parse_args(['--foo', 'spam']))

# invalid option
print(parser.parse_args(['--bar']))

# wrong number of arguments
print(parser.parse_args(['spam', 'badger']))

