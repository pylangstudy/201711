import argparse
parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group()
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
print(parser.parse_args(['--foo']))
print(parser.parse_args(['--bar']))
print(parser.parse_args(['--foo', '--bar']))

parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
print(parser.parse_args([]))
