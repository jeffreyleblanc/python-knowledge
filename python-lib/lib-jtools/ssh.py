# Copyright Jeffrey LeBlanc

class SSHInterface:

    def __init__(self, user="root", host=None):
        assert host is not None
        self.user = user
        self.host = host

    def __repr__(self):
        return f"<SSHInterface(user='{self.user}',host='{self.host}')>"


