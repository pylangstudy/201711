import argparse
import textwrap
parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--foo', type=int)
parser.add_argument('bar', type=float)
parser.print_help()
