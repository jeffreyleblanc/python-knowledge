#! /usr/bin/python3

'''
Shows a very basic interactive shell setup
'''

import code
import readline
import rlcompleter

class MyClass:

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':

    # Do some things
    myclass = MyClass('hello world')

    # Setup the interactive session
    vars = globals()
    vars.update(locals())
    readline.set_completer(rlcompleter.Completer(vars).complete)
    readline.parse_and_bind("tab: complete")
    shell = code.InteractiveConsole(vars)
    shell.interact()

