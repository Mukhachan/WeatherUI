import requests

url = "http://ip-api.com/line/?fields=city"

r = requests.get(url)
Gorod = r.text
print(Gorod)