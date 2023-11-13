import urllib.request
import requests

opener = urllib.request.build_opener()
resource = opener.open("https://httpbin.org/get")
print(resource.read())

resource = requests.get("https://httpbin.org/get")
print(requests.content)