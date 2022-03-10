import requests;
from PIL import Image,ImageFilter,ImageDraw,ImageFont;

image_path = './src/images/bg.jpg'
font_path = './src/'

def query_image_from_Unsplash(query: str, orientation: str):
    request_url = 'https://api.unsplash.com/photos/random?'
    client_id_fragment = '&client_id=DBmWBkEw9XM-RiyKjTitrQuPvzZtbd2FtClQX1a1an0'
    orientation_fragment = '&orientation=' + orientation
    query_fragment = '&query=' + query
    complete_url = request_url + client_id_fragment + orientation_fragment + query_fragment
    return requests.get(complete_url).json()

def get_image_caption(response):
    image_name = response.get('alt_description')
    image_author = response.get('user').get('name')
    if(image_name is None):
        return 'By '+image_author.upper()+' from Unsplash'
    elif(image_author is None):
        return image_name.upper()+' from Unsplash'
    elif(image_name is not None and image_author is not None):
        return image_name.upper()+' by '+image_author.upper()+' from Unsplash'

def download_and_write_image(image_path: str):
    image_url = response_json.get('urls').get('full')
    image_content = requests.get(image_url).content
    open(image_path,'wb').write(image_content)

def add_box_blur(image_path: str, blur_radius: int):
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.BoxBlur(blur_radius))
    # blurred_image.show()
    blurred_image.save(image_path)

def add_caption_on_image(image_path: str):
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Use AdobeVFPrototype.ttf, NotoSans-Regular.ttf or FreeMono.ttf
    font_family = font_path + 'NotoSans-Regular.ttf'
    font = ImageFont.truetype(font_family, 40)
    
    d1 = ImageDraw.Draw(image)
    d1.text((20, image_height-50), image_caption, fill=(0, 0, 0),font=font,stroke_width=1,stroke_fill=(256, 256, 256))
    # image.show()
    image.save(image_path)

response_json = query_image_from_Unsplash('dark texture','landscape')
image_caption = get_image_caption(response_json)
download_and_write_image(image_path=image_path)
add_box_blur(image_path=image_path, blur_radius=5)
add_caption_on_image(image_path=image_path)
print('Image: '+image_caption+' saved at '+image_path+' successfully')
exit(0)