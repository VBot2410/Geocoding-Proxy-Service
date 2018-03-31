
"""
google_api script that utilizes the google map API to send GET request


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
import json
import urllib.request
import os

# Get the Google API Key from environment
GOOGLE_KEY = os.environ.get("GOOGLE_KEY")


def geocode_by_google(input_location):
    """
    Use google map api to get the lat and long for the input_location.

    Parameters:
        input_location: A string specifying the address.

    Return:
        return a dictionary with keys: 'lat' and 'lng' with corresponding lat/long values
    """

    # replace all spaces with + to be compliant with google maps api
    location_string = input_location.replace(" ", "+")
    # insert the location string and the google api key
    raw_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
    url = raw_url.format(location_string, GOOGLE_KEY)

    try:
        # send a GET request and process the response into a json dictionary
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
    except Exception:
        return False

    if result['status'] == 'OK':
        # successful response
        lat_long_dict = result['results'][0]['geometry']['location']
        return lat_long_dict
    else:
        # not successful response
        print('Exception raised in geocode_by_google()')
        return False
