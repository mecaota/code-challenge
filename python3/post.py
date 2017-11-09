import urllib.request
import json

if __name__ == "__main__":
    data = [{"order":[103, 202, 302]}, {"order":[103, 208, 302]}]
    url = "http://localhost:5000/api/checkout"

    for p in data:
        p = json.dumps(p).encode("utf-8")
        print(p)
        req = urllib.request.Request(url, data=p, headers={"Content-Type" : "application/json"}, method="POST")
        with urllib.request.urlopen(req) as res:
            if res.getcode() == 200:
                res = json.loads(res.read().decode("utf-8"))
                print(str(res))
            else:
                print(res.getcode())
