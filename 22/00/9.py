import argparse
parser = argparse.ArgumentParser()
parser.add_argument('foo', type=int)
parser.set_defaults(bar=42, baz='badger')
print(parser.parse_args(['736']))

parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='bar')
parser.set_defaults(foo='spam')
print(parser.parse_args([]))

parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='badger')
print(parser.get_default('foo'))

