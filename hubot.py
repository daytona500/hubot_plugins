#!/usr/bin/env python

import httplib
import random
import re
import sys
import json
from xml.dom.minidom import parseString

tired = "Grab a 5 hour energy!"

def get_devopsborat():
    conn = httplib.HTTPConnection("api.twitter.com")
    conn.request("GET", "/1/statuses/user_timeline.json?screen_name=devops_borat")
    r1 = conn.getresponse()
    tweets = json.loads(r1.read())
    return tweets

def process_input(line):
    if re.match("borat", line):
        print (random.choice(get_devopsborat())["text"])

    if re.match("tired", line):
        print (tired)


def main():
    line = sys.argv[1]
    process_input(line)

if __name__ == "__main__":
    main()