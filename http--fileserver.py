#! /usr/bin/env python3

'''
Simple http file server with some options. Full Usage:

$ ./http--fileserver.py -p 8878 -d $HOME --open --allowed 127.0.0.1 192.168.1.168

Does basically what:
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /tmp/
does, but with some extras as a expandable platform

https://docs.python.org/3/library/http.server.html
https://github.com/python/cpython/blob/3.10/Lib/http/server.py
'''

import argparse
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

MyHandler = SimpleHTTPRequestHandler

class RejectHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_error(403)

    def do_HEAD(self):
        self.send_error(403)

class MyServer(HTTPServer):

    _ROOT_DIRECTORY = '/tmp'
    _ALLOWED_CLIENTS = None

    def finish_request(self, request, client_address):
        print('Request:',request)
        print('Client:',client_address)
        if self._ALLOWED_CLIENTS is not None:
            client_ip = client_address[0]
            if client_ip not in self._ALLOWED_CLIENTS:
                print('Reject!')
                # Might be a better way to do this
                RejectHandler(request,client_address,self)
                return
        self.RequestHandlerClass(
            request, client_address,self,directory=self._ROOT_DIRECTORY)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--port', help='port', type=int, default=8005)
    parser.add_argument('-d','--directory',help="Root directory to serve",default=Path.cwd())
    parser.add_argument('--open',action='store_true',help="Open server to exterior connections")
    parser.add_argument('--allowed',nargs="*",type=str,default=None)
    args = parser.parse_args()

    try:
        bind_addr = '' if args.open else '127.0.0.1'
        httpd = MyServer((bind_addr,args.port), MyHandler)
        httpd._ROOT_DIRECTORY = args.directory
        httpd._ALLOWED_CLIENTS = args.allowed
        print(f'Running at: localhost:{args.port}')
        print('NOTE THIS IS INSECURE!!! USE CAREFULLY!!!')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('shutting down')
        httpd.shutdown()

