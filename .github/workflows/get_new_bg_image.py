import json,sys,urllib3;

http = urllib3.PoolManager()
response = http.request('GET', 'https://api.unsplash.com/photos/random?client_id=DBmWBkEw9XM-RiyKjTitrQuPvzZtbd2FtClQX1a1an0')
print response.data
obj=json.load(response.data)
image_url = obj['urls.regular'])
print image_url
Img = http.request('GET',image_url)