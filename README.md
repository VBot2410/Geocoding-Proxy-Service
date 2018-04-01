# Geocoding-Proxy-Service
A simple network service that can resolve the lat, lng coordinates for an address by using third party geocoding services and RESTFul HTTP Interface.</br ></br >
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/90ec42f713d44be898afa2937a8d56bd)](https://www.codacy.com/app/VBot2410/Geocoding-Proxy-Service?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=VBot2410/Geocoding-Proxy-Service&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Overview
Geocoding is the process of converting addresses (like a street address) into geographic coordinates (like latitude and longitude), which you can use to place markers on a map, or position the map.</br >
This package provides a service that resolves the latitude and longitude for a given address using Google Maps Geocoding service, and uses HERE geocoding as a fallback if Google fails to resolve the address.</br >
### Geocoding Services Used
**1. Google Maps API**: More info on Google Maps Geocoder API can be found [here](https://developers.google.com/maps/documentation/geocoding/start)</br >
**2. HERE Geocoder API**: More info on HERE Geocoder API can be found [here](https://developer.here.com/documentation/geocoder/topics/quick-start-geocode.html)</br >
This project was developed using **Python3.5** and tested on a **Ubuntu 16.04 LTS** system.</br ></br >

## Dependencies
This project uses **standard python 3.5 libraries** and hence do not require any third-party libraries to work. List of standard libraries used is as follows:</br >
* json
* argparse
* http.server
* urllib.request

## Repository Cloning & Running the Server (Tested on Ubuntu 16.04 LTS with Python3.5)
### Cloning
```
git clone --recursive https://github.com/VBot2410/Geocoding-Proxy-Service.git
```
### Exporting the API Keys as environment variables
In order to use the Google and HERE APIs, API keys are required which can be obtained from their websites linked above.
After getting these keys, follow these instructions(For Ubuntu Systems):
```
echo -e "\nexport GOOGLE_KEY=\"<RECEIVED KEY>\"">>~/.bashrc
echo -e "\nexport HERE_APP_ID=\"<RECEIVED APP ID>\"">>~/.bashrc
echo -e "\nexport HERE_APP_CODE=\"<RECEIVED APP CODE>\"">>~/.bashrc
```
These will store the API keys in .bashrc and can be imported on that local machine as environment variables.
### Running the Server
After exporting the keys as environment variables, follow these instructions:
```
cd Geocoding-Proxy-Service
python3 main.py
```
This will start the server with default host 127.0.0.1 and port 5000.</br >
You can also specify the server host and port using --host and --port arguments as follows:</br >
```
python3 main.py --host 0.0.0.0 --port 8000
```
This will start the server with host 0.0.0.0 and port 8000</br >
For more information, use -h argument as follows:
```
python3 main.py -h
```
### Querying
After starting the server, service API can be called by using **GET** method and specifying *address* field using following URL syntax:
```
HOST:PORT/geocode?address=ADDRESS
```
Where HOST and PORT is the host and port used for launching the server in the previous step.
### Sample Output
For the query, output similar to this will be shown:</br >
**Query**:</br > http://127.0.0.1:5000/geocode?address=1600%20Amphitheatre%20Parkway%20Mountain%20View,%20CA%2094043 </br >
**Output**:</br >
{"API": "google", "status": "OK", "lng": -122.0856086, "lat": 37.4224082}
## Future Scope
1. Adding support for more APIs
2. Adding support for more RESTful HTTP interface methods like PUT, POST.
