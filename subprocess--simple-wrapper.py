#! /usr/bin/env python3

'''
Shows a simple wrapper around blocking subprocess calls.
Includes a streaming version of the output.
'''

#-- Helpers ------------------------------------------------------------------#

import os
TCOL = os.get_terminal_size().columns
def rule(text): print(f"\n{'-'*TCOL}\n{text}\n{'-'*TCOL}\n")


#-- SimpleProc ------------------------------------------------------------------#

import shlex
import subprocess

class SimpleProc:
    '''
    Blocking process caller.
    See <https://docs.python.org/3/library/subprocess.html> for details.
    '''

    __version__ = '0.1'

    @classmethod
    def run(cls, cmd, check=False):
        if isinstance(cmd,str): cmd = shlex.split(cmd)
        if check:
            result = subprocess.run(cmd,capture_output=True,check=True)
            return result.stdout.decode('utf-8')
        else:
            result = subprocess.run(cmd,capture_output=True)
            return (
                result.returncode,
                result.stdout.decode('utf-8'),
                result.stderr.decode('utf-8')
            )

    @classmethod
    def stream(cls, cmd, check=False):
        if isinstance(cmd,str): cmd = shlex.split(cmd)
        with subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE) as process:
            if check:
                while True:
                    output = process.stdout.readline().decode().strip()
                    rc = process.poll()
                    if output == '' and rc is not None:
                        break
                    if output:
                        yield output
                if rc != 0:
                    err = subprocess.CalledProcessError(returncode=rc,cmd=cmd)
                    err.stdout = process.stdout.read()
                    err.stderr = process.stderr.read()
                    raise err
            else:
                while True:
                    output = process.stdout.readline().decode().strip()
                    rc = process.poll()
                    if output == '' and rc is not None:
                        break
                    if output:
                        yield (rc,output)
                err = process.stderr.read().decode()
                yield (rc,err)

#-- Tests ---------------------------------------------------------------------------------------------------#

def test():
    P = SimpleProc

    lst = [
        ( P.run, 'ping google.com -c 3', dict() ),
        ( P.run, 'ping google.com -c 3', dict(check=True) ),
        ( P.stream, 'ping google.com -c 3', dict() ),
        ( P.stream, 'ping google.com -c 3', dict(check=True) ),
        ( P.run, 'ping yak -c 3', dict() ),
        ( P.run, 'ping yak -c 3', dict(check=True) ),
        ( P.stream, 'ping yak -c 3', dict() ),
        ( P.stream, 'ping yak -c 3', dict(check=True) )
    ]
    for meth,cmd,opts in lst:
        rule(f'{meth} | {opts} | {cmd}')

        if meth == P.run and opts == dict():
            r = meth(cmd,**opts)
            print(r)

        elif meth == P.run and opts == dict(check=True):
            try:
                r = meth(cmd,**opts)
                print(r)
            except subprocess.CalledProcessError as e:
                print('ERR:',e)
                print(e.stdout)
                print(e.stderr)

        elif meth == P.stream and opts == dict():
            for code,line in meth(cmd):
                print('>',code,line)

        elif meth == P.stream and opts == dict(check=True):
            try:
                for line in meth(cmd,check=True):
                    print('>',line)
            except subprocess.CalledProcessError as e:
                print('ERR:',e)
                print(e.stdout)
                print(e.stderr)


if __name__ == '__main__':
    test()

