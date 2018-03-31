"""
server script that starts the server using given host and port & keeps it running forever
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
