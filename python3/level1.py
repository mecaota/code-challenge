from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def message():
    return "post json to /api/checkout"

@app.route("/api/checkout", methods=['POST'])
def checkout():
    body = request.json
    
    return jsonify(body)

if __name__ == '__main__':
    #app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に