import argparse
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
checkout = subparsers.add_parser('checkout', aliases=['co'])
checkout.add_argument('foo')
print(parser.parse_args(['co', 'bar']))
