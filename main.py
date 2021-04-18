#DETECT TEXT FROM ANY IMAGE

import os, io
from google.cloud import vision_v1
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"Session_Account.json"

client = vision_v1.ImageAnnotatorClient()

file_name = 'test5.JPG'
image_path = f'./{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)

# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])
