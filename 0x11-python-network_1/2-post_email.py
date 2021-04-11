#!/usr/bin/python3
"""
   takes in a URL and an email, sends a POST request to the passed URL
   with the email as a parameter,
   and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(response.getheader('X-Request-Id'))
