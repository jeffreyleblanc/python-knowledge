#! /usr/bin/env python3

'''
https://docs.makotemplates.org/en/latest/usage.html#basic-usage
https://docs.makotemplates.org/en/latest/index.html

ADD:
    # Load the html template
    _tlookup = TemplateLookup(directories=['webresources/templates/'])
    self.HTML_TEMPLATE = _tlookup.get_template('page.html')
    self.INDEX_TEMPLATE = _tlookup.get_template('main.html')

Questions:
    Can we write directly to a file?
'''

from os import get_terminal_size
s = get_terminal_size()
NCOLS = s.columns

def R(): print(f"\n{'-'*NCOLS}\n")
def H(text): print(f"\n{'-'*NCOLS}\n{text}\n{'-'*NCOLS}\n")

from mako.template import Template


H('Basic String Completion')
mytemplate = Template("hello ${name}!")
print(mytemplate.render(name='Jack'))

H('Basic File Template')
mytemplate = Template(filename='mako--basics-template1.txt')
print(mytemplate.render(name='Jim',age=42))

H('Basic Syntax Options')
mytemplate = Template(filename='mako--basics-template2.html')
print(mytemplate.render(title='My Page',items=('Apple','Pear')))

H('Basic Template Lookup and Inheritance')
from mako.lookup import TemplateLookup
mylookup = TemplateLookup(directories=['.'])
mytemplate = Template(filename='mako--basics-template3-child.html',lookup=mylookup)
print(mytemplate.render(title="A cool page",items=('Car','Truck','Boat')))
