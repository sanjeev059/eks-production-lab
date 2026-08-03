from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

PAYMENT_SERVICE_URL = "http://payment-service/pay"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": "orders",
        "status": "healthy"
    }), 200


@app.route("/orders", methods=["POST"])
def create_order():

    order = request.get_json()

    print(f"Received Order : {order}")

    try:

        payment_response = requests.post(
            PAYMENT_SERVICE_URL,
            json={
                "amount": order.get("amount", 0)
            },
            timeout=5
        )

        if payment_response.status_code == 200:

            return jsonify({
                "order_id": "ORD-1001",
                "payment": "SUCCESS",
                "status": "CREATED"
            }), 201

        return jsonify({
            "error": "Payment Failed"
        }), 500

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)