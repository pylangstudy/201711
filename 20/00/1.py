import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
print(parser.parse_args('--foo 1'.split()))

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_const', const=42)
parser.parse_args(['--foo'])

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')
parser.parse_args('--foo --bar'.split())

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
parser.parse_args('--foo 1 --foo 2'.split())

parser = argparse.ArgumentParser()
parser.add_argument('--str', dest='types', action='append_const', const=str)
parser.add_argument('--int', dest='types', action='append_const', const=int)
parser.parse_args('--str --int'.split())

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')
parser.parse_args(['-vvv'])

import argparse
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
parser.parse_args(['--version'])

class FooAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(FooAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action=FooAction)
parser.add_argument('bar', action=FooAction)
args = parser.parse_args('1 --foo 2'.split())
args

