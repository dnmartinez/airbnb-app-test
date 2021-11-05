from flask import Flask, request, jsonify, make_response
app = Flask(__name__) # Create Flask app
from app import views

