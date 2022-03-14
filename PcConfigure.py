import requests

url = "http://ip-api.com/line/?fields=continent,country,city,lat,lon,isp,query"

r = requests.get(url)
PC_CONFIGURE = r.text
print(PC_CONFIGURE)