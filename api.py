import requests
import json
from RSSGathering import Gather


result = Gather()
url = "https://api.stitchdata.com/v2/import/batch"
myobj = {
    "table_name": 'podcast_episodes',
    "schema": {
      "properties": {
        "podcast_name": { "type": 'string' },
        "episode_guid": { "type": 'string' },
        "episode_title": { "type": 'string' },
        "episode_date": { "type": 'string', 'format': 'date-time' },
        "episode_mp3": { "type": 'string' }
      }
    },
    "messages": [
      
    ],
    "key_names": [
      'podcast_name', 
      'episode_guid'
    ]
  }
json_object = json.dumps(myobj)  
myobj['messages'] = result['messages']
x = requests.post(url, data = json_object, headers = {"Authorization": "Bearer 61df9635fca22916d96dc1ccb990c210e7b35b1acc82f9f968a5d2d6cea766fc", 'Content-Type': 'application/json'})

print(x.text)
#from pprint import pprint
#pprint(myobj)
#print(json_object)