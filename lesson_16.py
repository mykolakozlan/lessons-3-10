import os
import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1
from urllib.parse import urlparse

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_API_KEY = os.getenv("SECRET_API_KEY")

auth = OAuth1(API_KEY, SECRET_API_KEY)


img = '40'

endpoint = f"https://api.thenounproject.com/v2/icon/{img}"

response = requests.get(endpoint, auth=auth)

data = response.json()
icon_url = data['icon']['icon_url']
print(icon_url)
icon_response = requests.get(icon_url)

# print(icon_response.content)
pars = urlparse(icon_url)
icon_name = pars.path.split("/")[-1]
# icon_name = "test.svg"                    # розширення дуже важливо

with open(icon_name, 'wb') as f:
    f.write(icon_response.content)
