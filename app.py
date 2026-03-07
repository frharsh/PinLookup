from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/api/pincode/<pincode>", methods=["GET"])
def get_pincode(pincode):
    url = f"https://api.postalpincode.in/pincode/{pincode}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data[0]["Status"] == "Success":
            return jsonify({
                "success": True,
                "pincode": pincode,
                "postOffice": data[0]["PostOffice"]
            })
        else:
            return jsonify({
                "success": False,
                "message": "Invalid PIN Code"
            }), 404

    except requests.exceptions.Timeout:
        return jsonify({
            "success": False,
            "message": "Request Timeout — Try Again"
        }), 504

    except requests.exceptions.ConnectionError:
        return jsonify({
            "success": False,
            "message": "Connection Failed — India Post Server Down"
        }), 503

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Server Error",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)