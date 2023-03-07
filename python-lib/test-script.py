#! /usr/bin/env python3

from jtools.ssh import SSHInterface

def main():
    ssh = SSHInterface(user="jack",host="the-cloud")
    print(ssh)

if __name__ == "__main__":
    main()

