import requests;
from PIL import Image,ImageFilter;

# Set the stage
request_url = 'https://api.unsplash.com/photos/random?'
client_id_fragment = '&client_id=DBmWBkEw9XM-RiyKjTitrQuPvzZtbd2FtClQX1a1an0'
orientation_fragment = '&orientation=landscape'
query_fragment = '&query=dark+texture'
complete_url = request_url+client_id_fragment+orientation_fragment+query_fragment
output_filepath = './src/images/bg.jpg'
blurred_output_filepath = './src/images/bg_blurred.jpg'

# Actual implementation
response_json = requests.get(complete_url).json()
image_url = response_json.get('urls').get('regular')
ImageContent = requests.get(image_url).content
open(output_filepath,'wb').write(ImageContent)

#Open existing image
OriImage = Image.open(output_filepath)
OriImage.show()

#Applying BoxBlur filter
boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
boxImage.show()

#Save Boxblur image
boxImage.save(blurred_output_filepath)
