import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()
