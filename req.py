import requests

url = "http://localhost:5000/set_alert"
inp = input("Data to send: ")
data = {"event": inp} 
response = requests.post(url, json=data)

print(response.json()) 
