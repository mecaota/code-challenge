import database
from flask import Flask, request, jsonify
app = Flask(__name__)

### flaskサーバーメソッド
@app.route("/")
def message():
    return "Hell(t)o (go with) World"

@app.route("/api/checkout", methods=['POST'])
def checkout():
    body = request.json
    print(body)
    result = []
    for i in body["order"]:
        item, isItem = readMenu(i)
        if not isItem:
            return createRes(False)
        result.append(item)
    amount = sumAmount(result)
    return createRes(True, amount, body["order"])


### アプリメソッド
def sumAmount(req):
    sum = 0
    for i in req:
        sum = sum + i["price"]
    return sum

def readMenu(req):
    req = str(req)
    if req in database.db:
        return database.db[req], True
    else:
        return None, False

def createRes(ok, amount=0, items={}):
    res = {}
    res["ok"] = ok
    if ok:
        res["amount"] = amount
        res["items"] = items
    else:
        res["message"] = "item_not_found"
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)