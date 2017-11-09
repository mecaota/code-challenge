import urllib.request
import json
import sys

if __name__ == "__main__":
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
  url = "http://challenge-server.code-check.io/api/hash?" + urllib.parse.urlencode({"q":sys.argv[1]})
  print(url)

  with urllib.request.urlopen(url) as res:
    if(res.getcode() == 200):
      res = json.loads(res.read().decode("utf-8"))
      print(str(res["hash"]))
    else:
      print(res.getcode())