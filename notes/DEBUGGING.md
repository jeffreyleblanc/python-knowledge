# Debugging

## Most Basic Form: breakpoint

You can just insert `breakpoint()` anywhere in the code and run.


## PDB

```sh
# To run a script via pdb
$ python3 -m pdb your-script

# Then you can add breakpoints with filepath/line
> b /path/to/file.py:305

# To start the script
> c     # continue

# When you hit a breakpoint, combos of the following help
> l     # list where in code you are
> s     # step to next line in code
> u     # jump up a frame in the trace

# To evaluate a expression or just print value
> p expr

# To jump to next breakpoint
> n
```

For more commands: <https://docs.python.org/3/library/pdb.html#debugger-commands>

Resources

* <https://docs.python.org/3/library/pdb.html>
* Cheatsheets
    * <https://web.stanford.edu/class/physics91si/2013/handouts/Pdb_Commands.pdf>
* Learning
    * <https://github.com/spiside/pdb-tutorial>
    * <https://www.digitalocean.com/community/tutorials/how-to-use-the-python-debugger>
    * <https://codeburst.io/how-i-use-python-debugger-to-fix-code-279f11f75866>


## Developing Asyncio

This page has excellent advice: <https://docs.python.org/3/library/asyncio-dev.html>

One of the best is to `export PYTHONASYNCIODEBUG=1` which will provide more detailed feedback on issues
that can get "swallowed"


