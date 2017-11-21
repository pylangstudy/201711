import argparse
parser = argparse.ArgumentParser(prog='PROG')
print(parser.parse_args(['--help']))
print(parser.parse_args(['a', '--help']))
print(parser.parse_args(['b', '--help']))

