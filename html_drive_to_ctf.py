#import urllib.request
import http.client
import re
import sys
import time

AWAY = 'away'
TOO_FAST = 'too fast'
TOO_FAR = 'too far'
CLOSER = 'closer'  


def get_from_res(word, data):
  get_word = re.findall('name="{}" value="([^"]+)'.format(word), data)[0]
  return get_word  

def drive(lat, lon, token):
  url = 'drivetothetarget.web.ctfcompetition.com'
  conn = http.client.HTTPSConnection(url)
  
  # another option could be, check lat and log with 4 digit
  req2 = "/?lat={:.4f}&lon={:.4f}&token={}".format(lat, lon, token)	
  
  conn.request("GET", req2)
  r1 = conn.getresponse()
  
  data = r1.read().decode('utf-8')
  
  get_res = re.findall("<p>([^<]+)</p>", data)[0]
  get_lat = get_from_res('lat', data)
  get_lon = get_from_res('lon', data)
  get_token = get_from_res('token', data)
  
  r = None
  if AWAY in get_res:
      r = AWAY
  if TOO_FAST in get_res:
      r = TOO_FAST
  if TOO_FAR in get_res:
      r = TOO_FAR
  if CLOSER in get_res:
      r = CLOSER
  if r is None:
      print("===============got somting You went========")
      print(data)
      sys.exit()
  
  
  conn.close()
  return(r, float(get_lat), float(get_lon), get_token, get_res)

def main():
  # Direction vector
  v = [
      [1, 0],
      [0, 1],
      [-1, 0],
      [0, -1] 
    ]
  
  speed = 0.0001
  i = 0
  lat = 51.4914 
  lon = -0.1921
  #token = 'gAAAAABdY6hKUaTqwyWymLdu5VUXZ_SGZenh8ee3q1oTD39tTRSLGVJ_DiOOhe_zBmFngbV0DwEVaH20U6B3XKvt7pA16VLVqmYBFM6NkC8yRfZxTP3CE5KuIHVFtmORpap0uc5F_EBh'
  token = 'gAAAAABdZoPtD8gMEMCVJ_LI6MdryCpaYx-fOHy9p8LJAPzL9hd0wXQHUVXWxFYyBzRJvEGNwPzf_p3JbknTHBH5YRHiXCULJce9LpPJJyfoSELw3WqP8Yw45LzXEsfInVd6zQrG9By6'
  
  while True:
      new_lat = lat + v[i % 4][0] * speed
      new_lon = lon + v[i % 4][1] * speed
      r, lat, lon, token, res = drive(new_lat, new_lon, token)
      print(str(lat) + ',', lon, r, res, token)

      if r == AWAY:
          i += 1
          speed = 0.0001
          time.sleep(1)
          continue

      if r == CLOSER:
          speed = 0.0012
          time.sleep(10)
          continue

      if r == TOO_FAST:
        time.sleep(1)
        continue

  
main()
