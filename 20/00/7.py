import argparse
parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('--foo', action='store_true',
                    help='foo the bars before frobbling')
parser.add_argument('bar', nargs='+',
                    help='one of the bars to be frobbled')

parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('bar', nargs='?', type=int, default=42,
                    help='the bar to %(prog)s (default: %(default)s)')
parser.print_help()

parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('--foo', help=argparse.SUPPRESS)
parser.print_help()
