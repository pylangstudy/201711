import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    'integers', metavar='int', type=int, choices=range(10),
    nargs='+', help='an integer in the range 0..9')
parser.add_argument(
    '--sum', dest='accumulate', action='store_const', const=sum,
    default=max, help='sum the integers (default: find the max)')
print(parser.parse_args(['1', '2', '3', '4']))
print(parser.parse_args(['1', '2', '3', '4', '--sum']))

