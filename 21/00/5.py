import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
args = parser.parse_args(['--foo', 'BAR'])
print(vars(args))

class C:
    pass
c = C()
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
print(parser.parse_args(args=['--foo', 'BAR'], namespace=c))
print(c.foo)
