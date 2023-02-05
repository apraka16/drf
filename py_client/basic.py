import requests

"""A public API endpoint to play with"""
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://localhost:8000/api/'

# Client is requesting the endpoint for data
get_response = requests.get(endpoint, params={'abc': 123}, json={'query':'hello world'})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
