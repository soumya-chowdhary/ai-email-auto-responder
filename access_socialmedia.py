import requests

url = "https://graph.facebook.com/v19.0/8368408312/messages"

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "messaging_product": "whatsapp",
    "to": "918368408312",
    "type": "text",
    "text": {"body": "Hello from Python!"}
}

requests.post(url, headers=headers, json=data)
