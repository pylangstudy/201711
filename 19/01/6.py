import argparse
import textwrap
parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
print(parser.parse_args('+f X ++bar Y'.split()))
parser.print_help()
