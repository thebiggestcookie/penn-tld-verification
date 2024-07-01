import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for Penn TLD reels (you can expand this)
penn_tld_reels = [
    {
        "id": 1,
        "name": "Penn TLD15 Star Drag Reel",
        "attributes": [
            {"name": "Model", "value": "TLD15"},
            {"name": "Gear Ratio", "value": "3.8:1"},
            # ... add more attributes ...
        ]
    },
    # ... add more reels ...
]

@app.route('/api/reels', methods=['GET'])
def get_reels():
    return jsonify(penn_tld_reels)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
