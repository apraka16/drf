import requests


endpoint = 'http://localhost:8000/api/products/'

data = {
    "title": "New Product",
    # "content": "Not expensive",
    "price": 22.11
}

# Client is requesting the endpoint for data
get_response = requests.post(endpoint, json=data)
print(get_response.json())
