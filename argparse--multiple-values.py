#! /usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("targets",nargs="*",type=str)
    parser.add_argument('-f','--some-flag',action='store_true')
    args = parser.parse_args()
    print(args)

