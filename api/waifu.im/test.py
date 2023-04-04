import requests
import os
import shutil

url = 'https://cdn.waifu.im/6688.jpeg'
path = os.getcwd() + "/name.jpeg"


r = requests.get(url, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 
        print('Image Downloaded Successfully') 