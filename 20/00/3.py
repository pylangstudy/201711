import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=42)
parser.parse_args(['--foo', '2'])
parser.parse_args([])

parser = argparse.ArgumentParser()
parser.add_argument('--length', default='10', type=int)
parser.add_argument('--width', default=10.5, type=int)
parser.parse_args()

parser = argparse.ArgumentParser()
parser.add_argument('foo', nargs='?', default=42)
parser.parse_args(['a'])
parser.parse_args([])

parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=argparse.SUPPRESS)
parser.parse_args([])
parser.parse_args(['--foo', '1'])

