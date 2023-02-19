#! /usr/bin/env python3

import argparse
import logging

'''
See https://docs.python.org/3/howto/logging.html
'''

LOGGING_LEVELS_STR = ('DEBUG','INFO','WARNING','ERROR','CRITICAL')
LOGGING_LEVELS_NUM = (10,      20,    30,       40,     50)

def main():
    print('Logging!')
    logging.debug('I am a %s statement', 'debug')
    logging.info('I am a %s statement', 'info')
    logging.warning('I am a %s statement', 'warning')
    logging.error('I am a %s statement', 'error')
    logging.critical('I am a %s statement', 'critical')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--level', help='Logging level as string', default=None,
        choices=LOGGING_LEVELS_STR)
    parser.add_argument('-n','--num-level', help='Logging level as int', default=None,
        type=int,choices=LOGGING_LEVELS_NUM)
    args = parser.parse_args()

    if args.num_level is None and args.level is None:
        args.level = 'INFO'
    elif args.num_level is not None:
        logging.basicConfig(level=args.num_level)
    else:
        # Must setup before any logging occurs
        level = getattr(logging,args.level)
        logging.basicConfig(level=level)

    main()

