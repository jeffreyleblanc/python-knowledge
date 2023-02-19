#! /usr/bin/env python3

'''
A scaffold of tools for building simple terminal color utilities
'''

import sys
from os import get_terminal_size
from math import floor, ceil

class TerminalPrinter:

    TEXT = dict(
        # Core 8
        black =     '30',
        red =       '31',
        green =     '32',
        yellow =    '33',
        blue =      '34',
        magenta =   '35',
        cyan =      '36',
        white =     '37',
        # 'bright'
        b_black =    '90',
        b_red =      '91',
        b_green =    '92',
        b_yellow =   '93',
        b_blue =     '94',
        b_magenta =  '95',
        b_cyan =     '96',
        Wb_white =   '97'
    )

    STYLES = dict(
        normal =    '0',
        bold =      '1',
        lite =      '2',
        italic =    '3',
        underline = '4',
        blink =     '5',
        reverse =   '7'
    )

    def __init__(self):
        self.load_terminal_size()

    def lines(self, *args):
        ln = len(args)
        if ln == 1:
            print(args[0])
        elif ln == 2:
            style,text = args
            sparts = style.split()
            _STYLES = []
            for sp in sparts:
                if sp in self.TEXT:
                    _STYLES.append(self.TEXT[sp])
                elif sp in self.STYLES:
                    _STYLES.append(self.STYLES[sp])
            print(f"\x1b[{';'.join(_STYLES)}m{text}\x1b[0m")

    #-- Example of just making specific custom methods

    def red(self, text):
        print(f"\x1b[31m{text}\x1b[0m")

    def boldred(self, text):
        print(f"\x1b[31;1m{text}\x1b[0m")

    def green(self, text):
        print(f"\x1b[92m{text}\x1b[0m")

    def yellow(self, text):
        # yellow1
        print(f"\x1b[38;5;226m{text}\x1b[0m")

    def gray(self, text):
        # gray30
        print(f"\x1b[38;5;239m{text}\x1b[0m")

    def w(self, text):
        sys.stdout.write(text)

    def w_blue(self, text):
        # dodger_blue2
        self.w(f"\x1b[38;5;27m{text}\x1b[0m")

    #-- Example of simple interspersed colors ----------------#

    CMAP = {
        '[blue]': '\x1b[38;5;27m',
        '[bold]': '\x1b[1m',
        '[green]': '\x1b[92m',
        '[b_cyan]': '\x1b[96m',
        '[/]': '\x1b[0m'
    }

    def sprint(self, text):
        for k,v in self.CMAP.items():
            text = text.replace(k,v)
        text += '\x1b[0m'
        print(text)

    #-- Example of Formatting -------------------------#

    def load_terminal_size(self):
        s = get_terminal_size()
        self.col = s.columns
        self.row = s.lines


    def hr(self, sep='-'):
        return sep*self.col

    def header(self, text, sep='-'):
        width = self.col
        tl = len(text)
        if tl > width:
            text = text[:width]
        elif tl+4 > width:
            pass
        else:
            n = 0.5 * ( width - tl - 2 )
            text =  f"{sep*floor(n)} {text} {sep*ceil(n)}"
        return text

    def header2(self, text, sep='-'):
        self.load_terminal_size()
        width = self.col
        tl = len(text)
        if tl > width:
            text = text[:width]
        elif tl+4 > width:
            pass
        else:
            n = width - tl - 2
            text =  f"{sep*int(2)} {text} {sep*int(n-2)}"
        return text

if __name__ == '__main__':

    P = TerminalPrinter()

    P.lines('nothing')
    P.lines('red','This is red')
    P.lines('bold red','This is bold red')
    P.lines('b_green reverse','This is reverse bright green')

    P.red('Some red text')
    P.boldred('Some bold red text')
    P.green('Some green text')
    P.yellow('Some custom yellow text')

    P.w('One line white ')
    P.w_blue('BLUE')
    P.w(' Back to white')
    print()

    P.gray('Some gray text')

    P.yellow(P.hr())

    P.green(P.header('My Text'))

    P.red(P.header2('My Text'))

    P.sprint('[green]Green[/] normal [bold]bold![/] [b_cyan]Cyan')
    print('normal')

