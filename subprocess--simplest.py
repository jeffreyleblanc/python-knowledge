import subprocess
import shlex

def proc(cmd, cwd=None):
    '''
    cwd can be a Path and sets the working directory for the script
    Note that subprocess has other options for envars etc.
    '''
    if isinstance(cmd,str):
        cmd = shlex.split(cmd)
    r = subprocess.run(cmd,capture_output=True,cwd=cwd)
    return (
        r.returncode,
        r.stdout.decode('utf-8'),
        r.stderr.decode('utf-8')
    )

