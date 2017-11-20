import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')
parser.add_argument('foo', nargs='?')

# no negative number options, so -1 is a positional argument
print(parser.parse_args(['-x', '-1']))

# no negative number options, so -1 and -5 are positional arguments
print(parser.parse_args(['-x', '-1', '-5']))

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-1', dest='one')
print(parser.add_argument('foo', nargs='?'))

# negative number options present, so -1 is an option
print(parser.parse_args(['-1', 'X']))

# negative number options present, so -2 is an option
print(parser.parse_args(['-2']))

# negative number options present, so both -1s are options
print(parser.parse_args(['-1', '-1']))




print(parser.parse_args(['--', '-f']))
