import requests


endpoint = 'http://localhost:8000/api/products/'

# Client is requesting the endpoint for data
get_response = requests.get(endpoint)
print(get_response.json())
