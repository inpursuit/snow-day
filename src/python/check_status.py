import httplib
import RPi.GPIO as GPIO
import time
import sys

open_chan = 11
closed_chan = 13
button_chan = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(open_chan, GPIO.OUT)
GPIO.setup(closed_chan, GPIO.OUT)
GPIO.setup(button_chan, GPIO.IN)

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
GPIO.output(open_chan, False)
GPIO.output(closed_chan, False)

prev_state = 0
prev_checked_status = False
while True:
  state = GPIO.input(button_chan)
  if( (not prev_state) and state ):
    GPIO.output(open_chan, False)
    GPIO.output(closed_chan, False)
    if( prev_checked_status ):
      prev_checked_status = False
    else:
      prev_checked_status = True
      print "Checkiing status"
      value = checkstatus(url)
      if value == closed:
        print "  Schools are closed"
        GPIO.output(open_chan, False)
        GPIO.output(closed_chan, True)
      elif value == open:
        print "  Schools are open"
        GPIO.output(open_chan, True)
        GPIO.output(closed_chan, False)
      elif value == delay:
        print "  Schools are delayed"
        GPIO.output(open_chan, True)
        GPIO.output(closed_chan, True)
      else:
        print "  Unknown status"
        GPIO.output(open_chan, False)
        GPIO.output(closed_chan, False)
  prev_state = state
