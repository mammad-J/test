import requests
import json

docs = "https://animechan.vercel.app/docs"
url = "https://animechan.vercel.app/api/random"

response = requests.get(url).json()
print(response)
