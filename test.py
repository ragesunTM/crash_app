# coding: utf-8
import sys
import settings
import requests
import json

URL = "https://api.clashroyale.com/v1"


def main():
    access_key = settings.ACCESS_KEY
    target_api = URL+"/players/"
    playerTag = settings.PLAYERTAG
    url = target_api+playerTag
    headers = {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "max-age=60",
        "authorization": "Bearer  %s" % access_key}
    r = requests.get(url, headers=headers)
    data = r.json()

    l_nam = [d.get('iconUrls') for d in data['cards']]
    l_name = [d.get('medium') for d in l_nam]
    print(l_name)

    #print(json.dumps(data['cards'], indent=4))

if __name__ == '__main__':
    sys.exit(main())