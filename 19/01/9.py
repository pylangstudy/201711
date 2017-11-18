import argparse
import textwrap
parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
parser.add_argument('--foobar', action='store_true')
parser.add_argument('--foonley', action='store_false')
print(parser.parse_args(['--foon']))
