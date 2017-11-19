import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', required=True)
parser.parse_args(['--foo', 'BAR'])
parser.parse_args([])

