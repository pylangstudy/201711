import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')
parser.add_argument('--foo')
print(parser.parse_args(['-x', 'X']))
print(parser.parse_args(['--foo', 'FOO']))

print(parser.parse_args(['--foo=FOO']))

print(parser.parse_args(['-xX']))

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x', action='store_true')
parser.add_argument('-y', action='store_true')
parser.add_argument('-z')
print(parser.parse_args(['-xyzZ']))

