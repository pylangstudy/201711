import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('bar')
print(parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam']))
