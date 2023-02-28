#! /usr/bin/python3

import argparse
import markdown
from pathlib import Path
import subprocess
import shlex

'''
Initial sketch for an easy markdown publisher script/tool
'''

def proc(cmd, cwd=None):
    if isinstance(cmd,str):
        cmd = shlex.split(cmd)
    r = subprocess.run(cmd,capture_output=True,cwd=cwd)
    return (
        r.returncode,
        r.stdout.decode('utf-8'),
        r.stderr.decode('utf-8')
    )

PAGE = '''
<html>
<head>
<style>

    body {
        font-family: sans-serif;
        padding: 1rem;
    }

    pre {
        padding: 1rem;
        font-size: 0.9rem;
        background: #e2e8f0;
        border-radius: 0.25rem;
    }

    code {
        font-family: sans-serif;
        font-weight: bold;
        color: #1e3a8a;
    }

    a {
        color: #3b82f6;
    }

</style>
</head>
<body>
    PAGE_BODY
</body>
</html>
'''

def main():
    raise Exception('Test!')

    parser = argparse.ArgumentParser()
    parser.add_argument('source_file')
    parser.add_argument('-o','--output', help='Output file', default=None)
    parser.add_argument('--remote', help='Remote filepath', default=None)
    args = parser.parse_args()
    print(args)

    source = Path(args.source_file)
    with source.open('r') as f:
        src_text = f.read()

    html = markdown.markdown(src_text)
    page = PAGE.replace('PAGE_BODY',html)
    if args.output is None:
        print(page)
    else:
        with open(args.output,'w') as f:
            f.write(page)

    if args.remote is not None:
        if args.output is None:
            # Here could make a tmp file
            raise Exception()
        # args.remote like: 'user@fqdn:/var/www/my-site/html/root-dir'
        cmd = f'scp {args.output} {args.remote}'
        c,o,e = proc(cmd)
        if c!=0:
            print('ERROR SYNCING!')
            print(o)
            print(e)

if __name__ == '__main__':
    main()
