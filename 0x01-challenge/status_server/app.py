#!/usr/bin/python3
"""
Web server 
"""
from flask import Flask, jsonify, make_response
from api.v1.views import app_views

# Define the Flask application
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)

# Define the status endpoint
@app_views.route('/status', methods=['GET'])
def status():
    """Return server status"""
    return jsonify({"status": "OK"}), 200

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=5000)
