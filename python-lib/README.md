# Example Library

## Cheap Installation

Python libraries are stored at `/usr/lib/python3/dist-packages`.

While we can use `pip` or some other means to install, it is "cheap" for small local libraries to just sync them to the above path and then `chown -R root:root`. The `installation.sh` script here encapsulates that pattern.


