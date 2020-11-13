import requests
URL = "https://google.com"
page = requests.get(URL)
print(page.text)
