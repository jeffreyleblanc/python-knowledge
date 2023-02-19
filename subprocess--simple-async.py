#! /usr/bin/env python3

import shlex
import asyncio

async def aproc(cmd_str):
    # See: https://docs.python.org/3/library/asyncio-subprocess.html
    # Also see: https://docs.python.org/3/library/shlex.html#shlex.quote
    r = await asyncio.create_subprocess_shell(
        cmd_str,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await r.communicate()

    return (
        r.returncode,
        stdout.decode('utf-8'),
        stderr.decode('utf-8')
    )

async def main():
    cmds = [
        'ls /home/',
        'ip addr | grep 192.168',
        'echo "hello friends!"'
    ]
    for cmd in cmds:
        c,o,e = await aproc(cmd)
        print(c)
        print(o)
        print(e)

if __name__ == '__main__':
    asyncio.run(main())

