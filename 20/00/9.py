import argparse

parser = argparse.ArgumentParser()
parser.add_argument('bar')
parser.parse_args(['XXX'])

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo-bar', '--foo')
parser.add_argument('-x', '-y')
parser.parse_args('-f 1 -x 2'.split())
parser.parse_args('--foo 1 -y 2'.split())

parser = argparse.ArgumentParser()
parser.add_argument('--foo', dest='bar')
parser.parse_args('--foo XXX'.split())

