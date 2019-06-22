# -*- coding: utf-8 -*-

import sys
import json
import requests
import urllib
import urllib2

url = sys.argv[1]

values = {
     "from": "washer",
     "message": "洗濯が完了しました。"
     }

for line in sys.stdin:
    response = requests.post(url,
        json.dumps({'from':'washer', 'message': line}),
        headers={'Content-Type': 'application/json'}
        )
    if (response.status_code == 200):
        print(line)
    else:
        print(response.text)
