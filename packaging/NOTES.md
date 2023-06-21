# Python Build Rough Notes

## Links and Resources

* Tutorials
    * <https://packaging.python.org/en/latest/tutorials/packaging-projects/>
* Resources
    * <https://packaging.python.org/en/latest/key_projects/#build>


## Building the system

Get some needed dependencies:

```sh
sudo apt-get install python3-setuptools python3-build
```

Now before we build anything:

```sh
.
├── clean.sh
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
└── src
    └── jeffthing
        ├── example.py
        ├── __init__.py
        └── websrc
            └── my.css
```

And now we build it:

```sh
$ python3 -m build
```

And our directory now looks like:

```sh
.
├── clean.sh
├── dist
│   ├── jeffthing-0.0.1-py3-none-any.whl
│   └── jeffthing-0.0.1.tar.gz
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
└── src
    ├── jeffthing
    │   ├── example.py
    │   ├── __init__.py
    │   └── websrc
    │       └── my.css
    └── jeffthing.egg-info
        ├── dependency_links.txt
        ├── PKG-INFO
        ├── SOURCES.txt
        └── top_level.txt
```

## Trying Things In a Container

### Overview and Dependencies

I made a debian bookworm container, and then for purpose of exercise installed:

```sh
$ apt-get install python3-pip python3-tornado tree
```

Note that `pip` is huge (like 400mb) but seems needed for some of the following installations

### Python Search Path

Now before we try some things, it's worth noting how python find modules:

```sh
$ PYTHONPATH=/root/ python3 -c "import sys; print('\n'.join(sys.path))"
#> --this is '' --
#> /root
#> /usr/lib/python311.zip
#> /usr/lib/python3.11
#> /usr/lib/python3.11/lib-dynload
#> /usr/local/lib/python3.11/dist-packages
#> /usr/lib/python3/dist-packages
```

The above is the order that python will look for modules/packages. Of particular note are:

* `/usr/local/lib/python3.11/dist-packages`
* `/usr/lib/python3/dist-packages`

And note we can determine where a module comes from:

```sh
$ python3 -c "import math; print(math.__file__)"
#> Traceback (most recent call last):
#>   File "<string>", line 1, in <module>
#> AttributeError: module 'math' has no attribute '__file__'. Did you mean: '__name__'?

$ python3 -c "import pathlib; print(pathlib.__file__)"
#> /usr/lib/python3.11/pathlib.py

$ python3 -c "import tornado; print(tornado.__file__)"
#> /usr/lib/python3/dist-packages/tornado/__init__.py
```

For more details see <https://docs.python.org/3/library/sys_path_init.html#the-initialization-of-the-sys-path-module-search-path>.


### Installing Different Ways

Now we copy over the `.whl` file into the container and try to install it:

```sh
$ pip install jeffthing-0.0.1-py3-none-any.whl
#> Unhappy-ness... this machine has a package manager... etc

pip install jeffthing-0.0.1-py3-none-any.whl --break-system-packages
#> Just do it!
```

Now notice where things have ended up:

```sh
$ python3 -c "import jeffthing; print(jeffthing.__file__)"
#> /usr/local/lib/python3.11/dist-packages/jeffthing/__init__.py

$ ls -1 /usr/local/lib/python3.11/dist-packages/
#> jeffthing
#> jeffthing-0.0.1.dist-info

$ ls -1 /usr/lib/python3/dist-packages/
#> _distutils_hack
#> distutils-precedence.pth
#> pip
#> pip-23.0.1.dist-info
#> pkg_resources
#> setuptools
#> setuptools-66.1.1.egg-info
#> tornado
#> tornado-6.2.egg-info
#> wheel
#> wheel-0.38.4.egg-info
```

Now to remove jeffthing:

```sh
$ rm -rf /usr/local/lib/python3.11/dist-packages/jeffthing*
```

### Another way

We copy over the python project into the container and then:

```sh
# We must force install it with editable
$ python3 -m pip install -e .
$ python3 -m pip install -e . --break-system-packages

# And here is what got updated
$ ls -1 /usr/local/lib/python3.11/dist-packages/
#> __editable__.jeffthing-0.0.1.pth
#> jeffthing-0.0.1.dist-info

$ python3 -c "import jeffthing; print(jeffthing.__file__)"
#> /mnt/shared/jeffthing/src/jeffthing/__init__.py

python3 -c "import sys; print('\n'.join(sys.path))"
#> --is ''--
#> /usr/lib/python311.zip
#> /usr/lib/python3.11
#> /usr/lib/python3.11/lib-dynload
#> /usr/local/lib/python3.11/dist-packages
#> /mnt/shared/jeffthing/src
#> /usr/lib/python3/dist-packages

$ cat /usr/local/lib/python3.11/dist-packages/__editable__.jeffthing-0.0.1.pth
#> /mnt/shared/jeffthing/src
```

Now we can manually uninstall the packages parts, but what about using `pip`?

```sh
$ pip uninstall jeffthing --break-system-packages
#> Found existing installation: jeffthing 0.0.1
#> Uninstalling jeffthing-0.0.1:
#>   Would remove:
#>     /usr/local/lib/python3.11/dist-packages/__editable__.jeffthing-0.0.1.pth
#>     /usr/local/lib/python3.11/dist-packages/jeffthing-0.0.1.dist-info/*
#> Proceed (Y/n)? y
#>   Successfully uninstalled jeffthing-0.0.1
#> WARNING: Running pip as the 'root' user can result in broken permissions...

# And now note there is nothing on the paths
$ ls /usr/local/lib/python3.11/
$ python3 -c "import sys; print('\n'.join(sys.path))"
#> --is ''--
#> /usr/lib/python311.zip
#> /usr/lib/python3.11
#> /usr/lib/python3.11/lib-dynload
#> /usr/lib/python3/dist-packages
```

If we install again, `/usr/local/lib/python3.11/dist-packages` is recreated and added back into `sys.path`.


### Adding a Script

See in the `pyproject.toml` how this is entered and then note, in the container:

```sh
$ pip install jeffthing-0.0.1-py3-none-any.whl --break-system-packages --force-reinstall
#> --snip--

$ type jeffthing-tool
#> jeffthing-tool is /usr/local/bin/jeffthing-tool
```

And `/usr/local/bin/jeffthing-tool` is:

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from jeffthing.main_tool import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```


