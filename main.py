import time
from pycololight import PyCololight
from pdpyras import APISession
api_key = "ADD API KEY"
session = APISession(api_key, default_from="justynroberts@gmail.com")
# Setup hexagon device
light = PyCololight(device="hexagon", host="192.168.13.123")
# Turn on at 60% brightness
light.on = 100
while True:
    time.sleep(1)
    incidents = session.list_all(
    'incidents',
    params={'statuses[]':['triggered','acknowledged']}
)
    if len (incidents) == 0:
       light.colour = (0, 255, 0)
    for i in incidents:
        if i["status"] == "triggered":
            light.colour = (255, 0, 0)
        elif i["status"] == "acknowledged":
            light.colour = (255, 255, 0)
