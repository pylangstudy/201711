import argparse

class MyArgumentParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line):
        return arg_line.split()

parser = MyArgumentParser()
parser.add_argument('bar')

