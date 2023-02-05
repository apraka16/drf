import requests

endpoint = 'https://httpbin.org/anything'

# Client is requesting the endpoint for data
get_response = requests.get(endpoint, json={'query': 'hello world'})
# print(get_response.text)
print(get_response.json())
