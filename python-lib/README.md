# Example Library

## Cheap Installation

Python libraries are stored at `/usr/lib/python3/dist-packages`.

While we can use `pip` or some other means to install, it is "cheap" for small local libraries to just sync them to the above path and then `chown -R root:root`. The `installation.sh` script here encapsulates that pattern.

## Notes on The Module Search Path

* <https://docs.python.org/3/library/sys_path_init.html>
* <https://docs.python.org/3/library/sys.html#sys.path>

And also note the impact of setting `PYTHONPATH`:

```sh
$ python3 -c "import sys; print(sys.path)"
#> ['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']

$ PYTHONPATH=/tmp python3 -c "import sys; print(sys.path)"
#> ['', '/tmp', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

