import requests


endpoint = 'http://localhost:8000/api/products/12/'

# Client is requesting the endpoint for data
get_response = requests.get(endpoint)
print(get_response.json())
