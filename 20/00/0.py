import argparse
parser = argparse.ArgumentParser()
#オプション引数
print(parser.add_argument('-f', '--foo'))
#位置引数
print(parser.add_argument('bar'))

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo')
parser.add_argument('bar')
parser.parse_args(['BAR'])
parser.parse_args(['BAR', '--foo', 'FOO'])
parser.parse_args(['--foo', 'FOO'])

