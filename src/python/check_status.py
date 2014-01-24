import httplib
import RPi.GPIO as GPIO
import time
import sys

def checkstatus(url):
  conn = httplib.HTTPConnection("127.0.0.1")
  conn.request("GET","/status.php?url="+url)
  resp = conn.getresponse()
  value = resp.read()
  return value.lower()

closed = "closed"
open = "open"
delay = "delay"

url = sys.argv[1]
print "Using URL: "+url
while True:
  value = checkstatus(url)
  if value == closed:
    print "Schools are closed"
  elif value == open:
    print "Schools are open"
  elif value == delay:
    print "Schools are delayed"
  else:
    print "Unknown status"

  time.sleep(5)
