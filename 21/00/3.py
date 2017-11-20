import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-bacon')
parser.add_argument('-badger')
print(parser.parse_args('-bac MMM'.split()))
print(parser.parse_args('-bad WOOD'.split()))
print(parser.parse_args('-ba BA'.split()))

