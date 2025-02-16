import requests
import argparse

url = " http://localhost:5000/set_alert"
headers = {
    "ngrok-skip-browser-warning": "true",
    "Content-Type": "application/json"
}

parser = argparse.ArgumentParser(description="Send alert to server.")
parser.add_argument("event", choices=["default", "fire", "knock"], help="Event type to send")
args = parser.parse_args()

data = {"event": args.event}

try:
    response = requests.post(url, json=data, headers=headers, timeout=10)
    print("Response:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
