import requests
import json
import time


def find_artist(cod):
    r = requests.get("https://api.artsy.net/api/artists/" + cod, headers=headers)
    j = json.loads(r.text)
    return j['sortable_name'], j['birthday']


token = 'token'
headers = {"X-Xapp-Token": token}
artists = []
with open('dataset_24476_4.txt') as inp:
    for line in inp:
        cod = line.rstrip()
        artists.append(find_artist(cod))
        time.sleep(1)

artists.sort(key=lambda x: (x[1], x[0]))
with open('ans.txt', 'w') as ans:
    for line in artists:
        ans.write(line[0] + '\n')
