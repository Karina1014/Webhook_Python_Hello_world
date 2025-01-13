import requests
import json

webhook_url = 'http://127.0.0.1:9000/my-webhook'
data = {'message': 'Hello from client!'}

response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(f"Response from server: {response.json()}")
