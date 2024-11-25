from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    try:
        # Llamada al servicio product_catalog
        response = requests.get('http://product_catalog:5002/products')
        return jsonify({
            "message": "User management service is running",
            "products": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
