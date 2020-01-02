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

    #ここがわからん
    headers = {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "max-age=60",
        "authorization": "Bearer  %s" % access_key}
    r = requests.get(url, headers=headers)
    data = r.json()

    #命名要変更，内包表記もうちょい勉強
    l_nam = [d.get('iconUrls') for d in data['cards']]
    l_name = [d.get('medium') for d in l_nam]
    print(l_name)

    #元々のやつ
    #print(json.dumps(data['cards'], indent=4))

if __name__ == '__main__':
    sys.exit(main())