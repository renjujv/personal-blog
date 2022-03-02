import requests;
from PIL import Image,ImageFilter;

# Set the stage
request_url = 'https://api.unsplash.com/photos/random?'
client_id_fragment = '&client_id=DBmWBkEw9XM-RiyKjTitrQuPvzZtbd2FtClQX1a1an0'
orientation_fragment = '&orientation=landscape'
query_fragment = '&query=dark+texture'
complete_url = request_url+client_id_fragment+orientation_fragment+query_fragment
output_filepath = './src/images/bg.jpg'

# Actual implementation
response_json = requests.get(complete_url).json()
image_url = response_json.get('urls').get('regular')
image_content = requests.get(image_url).content
open(output_filepath,'wb').write(image_content)

#Open existing image
original_image = Image.open(output_filepath)
#Applying BoxBlur filter
blurred_image = original_image.filter(ImageFilter.BoxBlur(5))
#Save Boxblur image
blurred_image.save(output_filepath)
print('Image from '+image_url+' saved at '+output_filepath+' successfully')
exit(0)
