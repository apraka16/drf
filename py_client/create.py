import requests

"""A public API endpoint to play with"""
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "This field is done",
    "price": 32.99
}

# Client is requesting the endpoint for data
get_response = requests.post(endpoint, json=data)
print(get_response.json())
