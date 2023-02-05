import requests

product_id = input("What is the Product id you want to use?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"Product ID {product_id} is not valid")

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'

    # Client is requesting the endpoint for data
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)
