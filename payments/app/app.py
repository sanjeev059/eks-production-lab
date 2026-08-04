from flask import Flask
from prometheus_client import (
    Counter,
    Histogram,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
import time

app = Flask(__name__)

# -----------------------------
# Prometheus Metrics
# -----------------------------

# Total payment requests
payment_requests_total = Counter(
    "payment_requests_total",
    "Total number of payment requests"
)

# Successful payments
payment_success_total = Counter(
    "payment_success_total",
    "Total number of successful payment requests"
)

# Request latency
payment_request_duration_seconds = Histogram(
    "payment_request_duration_seconds",
    "Time spent processing payment requests"
)

# In-flight requests
payment_inprogress_requests = Gauge(
    "payment_inprogress_requests",
    "Current number of payment requests being processed"
)


# -----------------------------
# Application Endpoints
# -----------------------------

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

    # Increment current active requests
    payment_inprogress_requests.inc()

    start_time = time.time()

    try:
        # Count every request
        payment_requests_total.inc()

        # Simulate application processing
        time.sleep(0.1)

        # Count successful payment
        payment_success_total.inc()

        return {
            "paymentId": "PAY-1001",
            "status": "SUCCESS"
        }

    finally:
        # Observe request duration
        payment_request_duration_seconds.observe(
            time.time() - start_time
        )

        # Request completed
        payment_inprogress_requests.dec()


# -----------------------------
# Prometheus Metrics Endpoint
# -----------------------------

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


# -----------------------------
# Application Startup
# -----------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)