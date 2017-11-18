import argparse
#parser = argparse.ArgumentParser(
#    description='A foo that bars',
#    epilog="And that's how you'd foo a bar")
#parser.print_help()


parser = argparse.ArgumentParser(
    prog='PROG',
    description='''this description
        was indented weird
            but that is okay''',
    epilog='''
            likewise for this epilog whose whitespace will
        be cleaned up and whose words will be wrapped
        across a couple lines''')
parser.print_help()

