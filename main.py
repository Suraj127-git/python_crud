from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data stored in memory (replace with your own data)
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({"message": "Name is required"}), 400

    new_item = {
        'id': len(items) + 1,
        'name': data['name']
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"message": "Item not found"}), 404

    data = request.get_json()
    item['name'] = data.get('name', item['name'])
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
