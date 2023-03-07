#! /usr/bin/env python3

'''
https://docs.python.org/3/howto/regex.html
https://realpython.com/regex-python/
https://realpython.com/regex-python-part-2/
'''

import re

H = print

if __name__ == '__main__':
    l = '**r q** This has `python` &ast; and *italic* **oh *cool* no** and **bold** and `sd`   **t** and *use* and ***other*** horray. *bold*'

    # H('Capture first items between `')
    # r = re.search('\B`([^`]+)`\B',l)
    # print(r)
    # print()

    # H('Capture all items between `')
    # r = [e for e in re.finditer('\B`([^`]+)`\B',l)]
    # print(r)
    # print()

    # H('Capture all items between *')
    # r = [e for e in re.finditer('(^|\s)\*([^*]+)\*($|\s)',l)]
    # print(r)
    # print()

    # H('Capture all items between **')
    # r = [e for e in re.finditer('(^|\s)\*\*([^*]+)\*\*($|\s)',l)]
    # print(r)
    # print()

    # H('Capture all items between **. Does not quite work.')
    # r = re.sub('(?:^|\s)\*\*([^*]+)\*\*(?:$|\s)',lambda e: f" <A>{e.groups()[0]}</A> ",l)
    # print(r)
    # print()

    H('Capture all items between **. Does not quite work.')
    print(l)
    matches = [e for e in re.finditer(r'(\*{1,3})([^*]+)(\*{1,3})',l)]
    # matches = [e for e in re.finditer(r'(^|\s)\*\*([^*]+)\*\*($|\s)',l)]
    for m in matches:
        print(m)
        print(m.groups())
        start,end = m.span()
        print(f'>{l[start:end]}<')
    print()

    # l = 'this is a https://wapo.com link <https://cnn.com> etc... <sub>my stuff</sub>'

    # r = [e for e in re.finditer('<(http[^>]+)>',l)]
    # print(r)

    # r = [e for e in re.finditer('http\S+',l)]
    # print(r)

    # r = [e for e in re.finditer('https://\S+',l)]
    # print(r)

    # l = 'this is a https://wapo.com link <https://cnn.com> etc... <sub>my stuff</sub> [a $ link](https://jeff.org/cool)'

    # r = [e for e in re.finditer('\[\w+]\(https://\S+\)',l)]
    # print(r)

    # r = [e for e in re.finditer('\[[^\]]+\]\(https://\S+\)',l)]
    # print(r)

