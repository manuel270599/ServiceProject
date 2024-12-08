from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    try:
        return jsonify([
            {"id": 1, "nombre": "Product 1"},
            {"id": 2, "nombre": "Product 2"},
            {"id": 3, "nombre": "Product 3"},
            {"id": 4, "nombre": "Product 4"},
            {"id": 5, "nombre": "Product 5"}
            
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
