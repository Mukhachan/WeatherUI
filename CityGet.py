from requests import get
import geocoder

ip = get('https://api.my-ip.io/ip').text
g = geocoder.ipinfo(ip)
print(ip)
Gorod = g.city
print(Gorod)