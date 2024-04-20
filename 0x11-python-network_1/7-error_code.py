#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    response = get(argv[1])
    ERR_TXT = 'Error code: {}'
    status = response.status_code
    print(ERR_TXT.format(status) if (status >= 400) else response.text)
