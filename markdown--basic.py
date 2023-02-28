#! /usr/bin/env python3

from markdown import markdown

'''
Very basic markdown example with fenced code and highlights support

Review of markdown library
https://python-markdown.github.io/
https://python-markdown.github.io/extensions/code_hilite/

Review of syntax highlighting and useful links
https://pygments.org/
https://github.com/richleland/pygments-css
https://stylishthemes.github.io/Syntax-Themes/pygments/
https://github.com/PhilipTrauner/pygments-github-css
'''

# Here we use ~BACKTICKS~ to not confuse the markdown generator for this page
EXAMPLE_MARKDOWN_1 = '''
# Header 1

Some things *bold*

* Apple
* Orange
* Banana

## Header 2

Some `code` in a code fence:

~BACKTICKS~python
class MyClass:

    def __init__(self, value):
        self.value = value
~BACKTICKS~

'''

if __name__ == '__main__':

    MD = EXAMPLE_MARKDOWN_1.replace('~BACKTICKS~','```')
    html1 = markdown(MD,extensions=['fenced_code','codehilite'])
    print(html1)

    # To make configuration changes to a module:
    # extension_configs = {
    #     'codehilite' : {
    #         'guess_lang': False
    #     }
    # }
    # html = markdown(text,extensions=['fenced_code','codehilite'],extension_configs=extension_configs)
    # return html
