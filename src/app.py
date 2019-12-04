"""
Sample application file
"""


import requests


def handler(event, context):
    print(event)
    print(context)
    resp = requests.get("httpbin.org/json")
    print(resp.json())
