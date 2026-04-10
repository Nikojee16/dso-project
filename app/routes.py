from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/health")
def health():
    return jsonify({"status": "ok"})

@main.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})