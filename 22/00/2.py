import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                    description='valid subcommands',
                                    help='additional help')
subparsers.add_parser('foo')
subparsers.add_parser('bar')
print(parser.parse_args(['-h']))

