#! /usr/bin/env python3

import mistune
import json

'''
Mistune is a nicer seeming markdown tool than python-markdown

https://github.com/lepture/mistune
https://mistune.readthedocs.io/en/latest/index.html

Example of using pygments within the system:
https://mistune.readthedocs.io/en/latest/guide.html#customize-renderer

**NOTE** you need the following:
()$ pip list
Package    Version
---------- -------
mistune    2.0.4
pip        22.0.2
Pygments   2.13.0
setuptools 59.6.

'''

# Here we use ~BACKTICKS~ to not confuse the markdown generator for this page
MD = '''
# Heading 1

Some text.
And more text

* A list
* of lists
    * of things

## Heading 2

More text

~BACKTICKS~sh
$ cp $FILE
# does something
~BACKTICKS~

## Heading 3

Hello

> This is a block quote.
> Of something interesting.
> OR <https://nyt.com/> whatever
> alt [my page](/index/)

~BACKTICKS~
    nothing
    here
~BACKTICKS~

#### stuff

hi `apple pear` \* and **bold** people <https://wapo.com/> things &ast; are ok
'''

if __name__ == '__main__':
    MD = MD.replace('~BACKTICKS~','```')

    mark_html = mistune.create_markdown()
    html = mark_html(MD)
    print(html)

    # Mistune has this great feature of being able to dump the tree
    mark_ast = mistune.create_markdown(renderer=mistune.AstRenderer())
    obj = mark_ast(MD)
    print(json.dumps(obj,indent=4))

    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import html

    class HighlightRenderer(mistune.HTMLRenderer):
        def block_code(self, code, lang=None):
            if lang:
                lexer = get_lexer_by_name(lang, stripall=True)
                formatter = html.HtmlFormatter()
                return highlight(code, lexer, formatter)
            return f'<pre><code>{mistune.escape(code)}</code></pre>'

    mark2 = mistune.create_markdown(renderer=HighlightRenderer())
    html = mark2(MD)
    print(html)

    print('\n\n---\n\n')

    # See https://pygments.org/docs/quickstart/
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter

    code = 'print "Hello World"'
    print(highlight(code, PythonLexer(), HtmlFormatter()))
