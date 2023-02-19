#! /usr/bin/env python3

'''
Overview of basic pathlib methods

https://docs.python.org/3/library/pathlib.html
https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module
'''

from pathlib import Path
import uuid

def main():
    # Basics
    CWD = Path.cwd()
    THIS = Path(__file__)
    HERE = THIS.parent
    print('CWD',CWD)
    print('THIS',THIS)
    print('HERE',HERE)

    # More
    TMP = Path('/tmp')
    name = f'pathlib-example-{uuid.uuid4().hex[:6]}'
    TMP_DIR = TMP/name
    print('exists?',TMP_DIR.is_dir())
    TMP_DIR.mkdir(exist_ok=True)
    print('exists?',TMP_DIR.is_dir())

    # Home
    HOME1 = Path('~/').expanduser()
    HOME2 = Path.home()
    print('HOMES',HOME1,HOME2)
    print('equal?',HOME1==HOME2)

    # Basic Iteration
    for path in HOME1.iterdir():
        if path.is_file():
            print('file:',path)
            print('file.name:',path.name)
            print('file.suffix',path.suffix)
            print('file.suffixes',path.suffixes)
            print('files.stem',path.stem)
        elif path.is_dir():
            print('dir:',path)
        else:
            print('something:',path)

    '''
    text = path.read_text()
    _bytes = path.read_bytes()
    with some_path.open('w') as f:
        f.write(text)
    '''

if __name__ == '__main__':
    main()

