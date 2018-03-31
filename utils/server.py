"""
server script that starts the server using given host and port & keeps it running forever

MIT License

Copyright (c) 2018 Vaibhav Bhilare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
# imports
from http.server import HTTPServer
from utils.request_handler import RestHTTPRequestHandler


def run_server(host, port):
    """
    Use host and port to start the server and keep it running.

    Parameters:
        host: A string specifying the hostname.
        port: A string specifying the port.

    Return:
        None
    """
    httpd = HTTPServer((host, port), RestHTTPRequestHandler)
    print('Running server at host = {} and port = {}'.format(host, port))
    httpd.serve_forever()
