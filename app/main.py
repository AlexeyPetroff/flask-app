import logging
import os

from flask import Flask, Response

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger("http-server")

APP_NAME = os.getenv("APP_NAME", "airtasker")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    logger.info("Root endpoint hit")
    return Response(APP_NAME, status=200, mimetype="text/plain")


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    logger.debug("Healthcheck endpoint hit")
    return Response("OK", status=200, mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    logger.info(f"Starting server on port {port} with APP_NAME='{APP_NAME}'")
    app.run(host="0.0.0.0", port=port)