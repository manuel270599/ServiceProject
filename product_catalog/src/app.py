from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    try:
        return jsonify([
            {"id": 1, "name": "Product A"},
            {"id": 2, "name": "Product B"}
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
