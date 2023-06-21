# Python Core Topics

This page contains various notes on core topics

## How Python Knows (imports etc)

> This is focused on linux (Debian flavor in particular).

When you run a python script or entry point, how does it resolve `import` statements? A few notes on this topic.

First it will look in the local working directory.

Next it will look in `/usr/lib/python3/dist-packages`, for example:

```sh
$ python3 -c "import tornado; print(tornado.__file__)"
#> /usr/lib/python3/dist-packages/tornado/__init__.py
```

Shows where `tornado` is being resolved to.

If you want to direct python to search a specific path first you can:

```sh
$ PYTHONPATH=~/my-project python3 script.py

# Or:
$ export PYTHONPATH=~/my-project
$ python3 script.py
```


