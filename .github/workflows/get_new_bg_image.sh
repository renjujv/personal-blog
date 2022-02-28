#!/usr/bin/bash

#Get JQ to parse JSON response
apt-get install jq

# Remove existing new image
rm ../../src/images/bg_new.jpg

# Store image url
image_url = curl 'https://api.unsplash.com/photos/random?client_id=DBmWBkEw9XM-RiyKjTitrQuPvzZtbd2FtClQX1a1an0' | jq -r '.urls.regular'

#download image to new file in images
curl $image_url -o ../../src/images/bg_new.jpg
