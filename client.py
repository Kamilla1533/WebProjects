import requests

# обращение к серверу
res  = requests.get("http://127.0.0.1:8000/api/main/2")
print(res.json())