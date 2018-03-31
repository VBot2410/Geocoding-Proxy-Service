"""
here_api script that utilizes the here map API to send GET request


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
import json
import urllib.request
import os

# Get the HERE APP KEY & APP CODE from environment
HERE_APP_ID = os.environ.get("HERE_APP_ID")
HERE_APP_CODE = os.environ.get("HERE_APP_CODE")

def geocode_by_here(input_location):
    """
    Use here api to get the lat and long for the input_location.

    Parameters:
        input_location: A string specifying the address.

    Return:
        return a dictionary with keys 'lat' and 'lng' with corresponding lat/long values.
    """

    # replace all spaces with + to be compliant with google maps api
    location_string = input_location.replace(" ", "+")
    # insert the location string and the here api key
    raw_url = 'https://geocoder.cit.api.here.com/6.2/geocode.json?'\
            'app_id={}&app_code={}&searchtext={}'
    url = raw_url.format(HERE_APP_ID, HERE_APP_CODE, location_string)

    try:
        # send a GET request and process the response into a json dictionary
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
        lat_long_dict = result['Response']['View'][0]['Result'][0]\
            ['Location']['NavigationPosition'][0]
        return lat_long_dict
    except Exception:
        print('Exception raised in geocode_by_here().')
        return False
