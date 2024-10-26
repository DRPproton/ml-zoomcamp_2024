import requests

url = 'http://localhost:9696'


response = requests.get(url).json()
print(response)