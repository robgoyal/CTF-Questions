import os

from flask import Flask, request, abort, jsonify, send_from_directory

NEXT_PASSWORD = '<ARG_NEXT_USER_PASSWORD>'

api = Flask(__name__)

@api.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"error": "There's nothing here. Submit your request to /<filename>"})

@api.route("/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file."""

    if filename != "blacktuque.doc":
        return jsonify({"error": "The filename must be blacktuque.doc"})

    if request.headers.get("Content-Type", "") != "multipart/form-data":
        return jsonify({"error": "The content type must be multipart/form-data"})

    data = request.data.decode()
    if data != "BLACKTUQUE 2023":
        return jsonify({"error": "The contents of the file must be 'BLACKTUQUE 2023'"})

    return jsonify({"success": f"The password for the next user is: {NEXT_PASSWORD}"})

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80)
