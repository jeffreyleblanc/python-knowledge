#! /usr/bin/env python3

'''
This script walks through the major point of using color and sizing text in the terminal.

## A) Add

    how terminal color support
    tmux example
    sys.stdout.write vs print

## 1) Basic Styles Overview

    The ANSI color standard is used by terminals, and the basics follow:

    Color digit:

        0   black
        1   red
        2   green
        3   yellow
        4   blue
        5   magenta
        6   cyan
        7   white

    Range digits:

        3   standard text
        9   bright text
        4   standard background
        10  bright background

    So for example '32' is standard green and '106' is bright magenta background

    To style the text, the following codes apply

        0   NORMAL
        1   BOLD
        2   LITE
        3   ITALIC
        4   UNDERLINE
        5   BLINK
        7   REVERSE

## 2) Patterns

    Note that \033 and \x1b and \u001b function the same in a string. I use \x1b as it's a bit shorter

    CTRL_START = "\x1b["
    CTRL_END = "m"
    STYLE_RESET = f"{CTRL_START}0{CTRL_END}"

## 2.1) 16 color map with one style block

    f'{CTRL_START}<style_list>{CTRL_END}<text>{STYLE_RESET}'

    where examples of style_list are:

    32          green text
    32;4        green text, italic
    92;46;1     bright green text, cyan background, bold

    and to make it clear, the last one looks like:

    "\x1b[92;46;1mMy Text\x1b[0m"

    or in general:

    STYLE = f'{CTRL_START}{background};{foreground};{style}{CTRL_END}'

    Note the order of the styles doesn't matter

## 2.2) 16 color map with multiple style blocks

    You can also apply multiple style in seperate blocks

    So "\x1b[92;46;1mMy Text\x1b[0m" can also be:

    "\x1b[92m\x1b[46m\x1b[1mMy Text\x1b[0m"

    When using 256 based color, this technique is needed

## 2.3) 256 Colors

    To get 256 colors, the following pattern is used

    text            \x1b[38;5;{color_code}m
    background:     \x1b[48;5;{color_code}m


## 3) Resources and Links

    * Excellent break down of color code patterns:
        * https://chrisyeh96.github.io/2020/03/28/terminal-colors.html
    * Good code examples:
        * https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#16-colors
    * More useful examples:
        * http://jafrog.com/2013/11/23/colors-in-terminal.html
'''

if __name__ == '__main__':

    import sys

    from os import get_terminal_size
    s = get_terminal_size()
    NCOLS = s.columns
    NROWS = s.lines

    def DIVIDE(): print(f"\n{'='*NCOLS}\n")

    DIVIDE()
    print('# Walk through the basic 16 colors and styles')

    COLOR16MAP = dict(
        colors = dict(
            BLACK =     '0',
            RED =       '1',
            GREEN =     '2',
            YELLOW =    '3',
            BLUE =      '4',
            MAGENTA =   '5',
            CYAN =      '6',
            WHITE =     '7'
        ),
        bright = dict(
            DEFAULT =    '3',
            BRIGHT =     '9',
            BACKGROUND = '4',
            BRIGHT_BACKGROUND = '10'
        ),
        styles = dict(
            NORMAL =    '0',
            BOLD =      '1',
            LITE =      '2',
            ITALIC =    '3',
            UNDERLINE = '4',
            BLINK =     '5',
            REVERSE =   '7'
        )
    )

    for clr_name, clr_id in COLOR16MAP['colors'].items():
        for br_name,br_id in COLOR16MAP['bright'].items():
            for style_name,style_id in COLOR16MAP['styles'].items():
                text = br_name+'_'+clr_name+'_'+style_name
                line = f'\x1b[{br_id}{clr_id};{style_id}m{text}\x1b[0m'
                print(line)

    DIVIDE()
    print('# Using sys.stdout.write')
    sys.stdout.write("A ")
    sys.stdout.write("\x1b[31mB\x1b[0m")
    sys.stdout.write(" C")
    sys.stdout.write('\n')
    sys.stdout.write('1\n')

    DIVIDE()
    print('# Example of different styles on the same line:')
    print("\x1b[31mHello\x1b[0m World \x1b[3;35mThings\x1b[0m")

    DIVIDE()
    print('# Example of closing style across lines')
    print("\x1b[36m")
    print("This will be cyan")
    print("As well as this!")
    print("\x1b[0m")
    print('back to default')

    DIVIDE()
    print('# Example of multi line string')
    text = "apple pear\ndog\n\tninja\nwater."
    print(f"\x1b[36m{text}\x1b[0m")
    print('back to default')

    DIVIDE()
    print('# Example that only need to reset at end')
    print("\x1b[34m Blue \x1b[35m Magenta \x1b[36;1m Bold Cyan \x1b[36;0m Cyan \x1b[37;0m White \x1b[0m")
    print('back to default')

    DIVIDE()
    print('# clean up example of multiple styles')

    print("\x1b[40m A \x1b[41m B \x1b[42m C \x1b[43m D \x1b[0m")
    print("\x1b[44m A \x1b[45m B \x1b[46m C \x1b[47m D \x1b[0m")
    print("\x1b[40;97;1m A \x1b[41;1m B \x1b[42;1m C \x1b[43;1m D \x1b[0m")
    print("\x1b[44;1m A \x1b[45;1m B \x1b[46;1m C \x1b[47;1m D \x1b[0m")

    # blue background '44', bright red text '91', bold '1'
    print("\x1b[44;91;1m WHAT ABOUT THIS?? \x1b[0m")
    print("\x1b[1;44;91m WHAT ABOUT THIS?? \x1b[0m")
    print("\x1b[91;44;1m WHAT ABOUT THIS?? \x1b[0m")
    print("\x1b[91m\x1b[44m\x1b[1m WHAT ABOUT THIS?? \x1b[0m")

    DIVIDE()
    print('# 256 text colors')
    for i in range(16):
        for j in range(16):
            code = str(i*16+j)
            sys.stdout.write(f"\x1b[38;5;{code}m{code.ljust(4)}")
        print("\x1b[0m")

    DIVIDE()
    print('# 256 background colors')
    for i in range(16):
        for j in range(16):
            code = str(i*16+j)
            sys.stdout.write(f"\x1b[48;5;{code}m{code.ljust(4)}")
        print("\x1b[0m")

    DIVIDE()
    print('Experiments')

    K,E = ("\x1b[","\x1b[0m")
    print(f"{K}38;5;226m WHAT ABOUT THIS?? {E}")
    print(f"{K}38;5;226m {K}44m {K}3m WHAT ABOUT THIS?? {E}")
    print(f"{K}38;5;226m{K}48;5;200m{K}3m{K}1m WHAT ABOUT THIS?? {E}")
    print("\x1b[38;5;226m\x1b[48;5;200m\x1b[3m\x1b[1m WHAT ABOUT THIS?? \x1b[0m")

    DIVIDE()
    print('# experiments')
    print("\x1b[31m ALPHA \x1b[0m")
    print("\x1b[91m ALPHA \x1b[0m")
    print("\x1b[41m ALPHA \x1b[0m")
    print("\x1b[101m ALPHA \x1b[0m")
    print("\x1b[1m BOLD \x1b[0m\x1b[4m Underline \x1b[0m\x1b[7m Reversed \x1b[0m")
    print("\x1b[1m\x1b[4m\x1b[7m BOLD Underline Reversed \x1b[0m")
    print("\x1b[1m\x1b[31m Red Bold \x1b[0m")
    print("\x1b[4m\x1b[44m Blue Background Underline \x1b[0m")

