from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/set_alert', methods=['POST'])
def set_alert():
    data = request.get_json()
    if "event" in data and data["event"] in ["fire", "knock","default"]:
        with open("alert.json", "w") as f:
            json.dump({"event": data["event"]}, f)
        return jsonify({"status": "success", "alert": data["event"]}), 200
    return jsonify({"status": "error", "message": "Invalid event"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
