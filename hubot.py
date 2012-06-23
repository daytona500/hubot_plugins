#!/usr/bin/env python

import httplib
import random
import re
import sys
import json


def get_devopsborat():
    """Returns tweets from Devops Borat."""
    conn = httplib.HTTPConnection("api.twitter.com")
    conn.request("GET", "/1/statuses/user_timeline.json?screen_name=devops_borat")
    r1 = conn.getresponse()
    tweets = json.loads(r1.read())
    return tweets

def get_mileycyrus():
    """Returns tweets from Miley Cyrus."""
    conn = httplib.HTTPConnection("api.twitter.com")
    conn.request("GET", "/1/statuses/user_timeline.json?screen_name=MileyCyrus")
    r1 = conn.getresponse()
    tweets = json.loads(r1.read())
    return tweets

def process_input(line):
    """Sends tweet after name is given and after 1 in 25 lines."""
    random_number = int(random.random() * 100)
    
    if random_number > 98:
        print "Borat: " + (random.choice(get_devopsborat())["text"])
    if random_number < 2:
        print "Miley Ray: " + (random.choice(get_mileycyrus())["text"])
    if re.match("borat", line):
        print (random.choice(get_devopsborat())["text"])
    if re.match("miley", line):
        print (random.choice(get_mileycyrus())["text"])

def main():
    line = sys.argv[1]
    process_input(line)

if __name__ == "__main__":
    main()