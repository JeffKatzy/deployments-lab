from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/apartments')
def apartments():
    return jsonify([{'id': 1, 'address': '164 W. 26th Street', 'zipcode': 10001, 'bedrooms': 4, 'bathrooms': 2}, 
        {'id': 2, 'address': '335 E. 22nd Street', 'zipcode': 10010,  'bedrooms': 'studio', 'bathrooms': 1}, 
        {'id': 3, 'address': '134 W. 83rd Street', 'zipcode': 10014,  'bedrooms': '3br', 'bathrooms': 2}, 
        {'id': 4, 'address': '22 W. 66th Street', 'zipcode': 10055,  'bedrooms': '1br', 'bathrooms': 1}, 
        ])
