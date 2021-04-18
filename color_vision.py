import os , io
from google.cloud import vision_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"Session_Account.json"

client = vision_v1.ImageAnnotatorClient()

file_name = 'test2.JPG'
image_path = f'./{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.Image(content=content)

response = client.image_properties(image=image)
props = response.image_properties_annotation
print('Properties:')

for color in props.dominant_colors.colors:
    print('fraction: {}'.format(color.pixel_fraction))
    print('\tr: {}'.format(color.color.red))
    print('\tg: {}'.format(color.color.green))
    print('\tb: {}'.format(color.color.blue))
    print('\ta: {}'.format(color.color.alpha))
