#! /usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', help='port', type=int)
    parser.add_argument('-f','--flag', action='store_true', help='Autoreload server code')
    parser.add_argument('--autoreload', action='store_true', help='Autoreload server code')
    parser.add_argument('--ip', help='IP', default=None)

    args = parser.parse_args()
    print(args)

