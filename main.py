import requests

resource = requests.get("https://httpbin.org/get")
print(requests.text)
print(f"DataType - {type(resource.content)}")

