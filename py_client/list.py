import requests

"""A public API endpoint to play with"""
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://localhost:8000/api/products/'

# Client is requesting the endpoint for data
get_response = requests.get(endpoint)
print(get_response.json())
