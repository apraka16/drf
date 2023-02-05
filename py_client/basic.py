import requests

"""A public API endpoint to play with"""
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://localhost:8000/api/'

# Client is requesting the endpoint for data
get_response = requests.post(endpoint, json={'title': "ABC123", "content": "Hello world", "price": "ac1234"})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
# print(get_response.headers)
