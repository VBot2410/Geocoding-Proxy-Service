"""
request handler script

It utilizes the primary and secondary api to retrieve latitude &
longitude data using RESTFul HTTP interface.


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
import urllib.request
import json
from http.server import BaseHTTPRequestHandler
from utils.geocoder.google_api import geocode_by_google
from utils.geocoder.here_api import geocode_by_here


class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    used to handle the HTTP requests that arrive at the server


    Parameters:
        BaseHTTPRequestHandler: A request

    Return:
        None
    """

    def do_GET(self):
        """ GET request method """

        # send back the header with status code 200
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'json')
        self.end_headers()

        if self.path[:9] != '/geocode?':
            # wrong syntax - provide help
            self.wfile.write(json.dumps(provide_help()).encode('utf-8'))
        else:
            # parse the GET arguments and isolate the address
            args = urllib.parse.parse_qs(self.path[9:])
            if 'address' in args:
                # address argument is passed on
                result = get_lat_long(str(args['address'][0]))
                if result:
                    # success
                    result['status'] = 'OK'
                else:
                    # failure
                    result = {'status': 'unsuccessful'}
                self.wfile.write(json.dumps(result).encode('utf-8'))
            else:
                # no address argument is passed on
                result = {'status': 'address is missing'}
                self.wfile.write(json.dumps(result).encode('utf-8'))
        return


def get_lat_long(input_location):
    """
    Use google maps api as primary service to return the lat and long of the input_location.
    if not successful, use here api as secondary fallback to get lat and long

    Parameters:
        input_location: A string specifying the address.

    Return:
        return a dictionary with keys 'lat' and 'lng' with corresponding lat/long values.
    """

    # primary api. use google maps api first
    result_g = geocode_by_google(input_location)
    if result_g:
        # success
        result_g['API'] = 'google'
        # return google result
        return result_g
    else:
        # secondary api. use here api as secondary fallback
        result_h = geocode_by_here(input_location)
        if result_h:
            result_h['API'] = 'here'
        # return here result
        return result_h


def provide_help():
    """
    send an api syntax error status and show the correct usage of the api

    Return:
        return a dictionary with keys 'syntax', 'status' , 'description' specifying error & help
    """
    # reference syntax
    syntax_str = 'HOST:PORT/geocode?address=ADDRESS'
    # description of parameters
    description_str = 'Use the correct syntax in which, '
    description_str += ' HOST is the host server ip address - '
    description_str += ' PORT is the port to use - '
    description_str += ' ADDRESS is the address to be geocoded.'
    # result dictionary
    result = {'syntax': syntax_str, 'status': 'api syntax error', 'description': description_str}
    # return help result
    return result
