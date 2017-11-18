import argparse
parser = argparse.ArgumentParser(prog='PROG', add_help=False)
parser.add_argument('--foo', help='foo help')
parser.print_help()
