#!/usr/bin/env python

import httplib
import random
import re
import sys
from xml.dom.minidom import parseString

jokes = ["FUCK IT! We'll do it live!",
         "*makes it rain*",
         "There can only by 100 bindings!?!? We're FUCKED! FUCKED!",
         "Ummm.... Ruby has segfaulted...",
         "WWJBD?",
         "Sacramento datacenter is 100% operational",
         "Pantheon looks great and all, but does it have node?",
         "DEVELOPERS! DEVELOPERS! DEVELOPERS! DEVELOPERS!",
         "Sensunati Pantheon tell me, YOU HAVE ERRORS: http://www.quickmeme.com/meme/3pc418/",
         "'Huh. I've never seen that running in production before.'"
        ]

weather = "You should get outside and go on a run."

food = "I think you could use a few more salads."

tired = "Grab a 5 hour energy!"

def get_weather():
    conn = httplib.HTTPConnection("www.google.com")
    conn.request("GET", "/ig/api?weather=Oakland")
    r1 = conn.getresponse()
    return r1.read()

def process_input(line):
    if re.match("hubot plugins", line):
        print " * inside joke: tell us an inside joke"

    if re.match("inside joke", line):
        print random.choice(jokes)
        
    if re.match("weather", line):
        dom = parseString(get_weather())
        degrees = dom.getElementsByTagName('temp_f')[0].getAttributeNode('data').nodeValue
        print "It is %s degress in Oakland" % (degrees)

    if re.match("tired", line):
        print (tired)


def main():
    line = sys.argv[1]
    process_input(line)

if __name__ == "__main__":
    main()