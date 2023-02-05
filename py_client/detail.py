import requests

"""A public API endpoint to play with"""
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://localhost:8000/api/products/1/'

# Client is requesting the endpoint for data
get_response = requests.get(endpoint, json={'title': "ABC123", "content": "Hello world", "price": "ac1234"})
print(get_response.json())
