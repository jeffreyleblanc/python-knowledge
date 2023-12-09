# Virtual Enviornments

## Making and using a Python venv

Note that on Debian/Ubuntu you need to install:

```sh
$ apt-get install python3-venv
```

> Note: There are other packages, such as `python3-virtualenv`,
> but I think the above is best

Then to make and use:

```sh
# Initial setup
$ python3 -m venv venv
$ source venv/bin/activate
$ PS1='()$ '

# Upgrade pip
()$ pip install --upgrade pip

# Check on pip
()$ pip3 list

# Install some things
()$ pip3 install Sqlalchemy
()$ pip3 install pyexcel-ods3

# Document libraries being used
()$ pip3 freeze > requirements.txt

# Or, if you aleady have a requirements.txt
()$ pip3 install -r requirements.txt

# If you want to 'turn off' the venv
()$ deactivate
```

And note where you are in the venv:

```sh
()$ pwd
#> MYLOC

()$ which python3 pip pip3
#> MYLOC/venv/bin/python3
#> MYLOC/venv/bin/pip
#> MYLOC/venv/bin/pip3

()$ deactivate

$ which pip python3 pip3
#> /usr/bin/python3
```

## Questions

* Should we use `pip` or `pip3`?
    * use `pip3`
* Note that `pip3 search` doesn't work anymore
    * Better off to look at <https://pypi.org/>

