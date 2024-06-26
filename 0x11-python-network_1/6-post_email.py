#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

if __name__ == '__main__':
    from sys import argv
    from requests import post

    res = post(argv[1], {'email': argv[2]})
    print(res.text)
