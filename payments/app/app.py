from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "service": "payment-api",
        "version": "1.0.0",
        "status": "UP"
    }


@app.route("/health")
def health():
    return "OK", 200


@app.route("/payment")
def payment():
    return {
        "paymentId": "PAY-1001",
        "status": "SUCCESS"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)