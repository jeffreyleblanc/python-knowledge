'''
Basic subparser example
'''

import argparse

def main():
    parser = argparse.ArgumentParser(description='My command line tool.')
    subparsers = parser.add_subparsers(help='sub-command help',dest='main_command')
    # version
    p = subparsers.add_parser('version', help='Show version info')
    # Command 1
    p = subparsers.add_parser('command1', help='The first command')
    p.add_argument('thing_name',help='Thing name')
    p.add_argument('--kind',help='Kind of thing',choices=('A','B'),default='A')
    # Command 2
    p = subparsers.add_parser('command2', help='The second command')
    p.add_argument('name1',help='Name 1')
    p.add_argument('name2',help='Name 2')
    # process
    args = parser.parse_args()

    if args.main_command is None:
        # Can also `parser.print_usage()`
        parser.print_help()
    else:
        print(args)

if __name__ == '__main__':
    main()

