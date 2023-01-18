from flask import Flask, request

app = Flask(__name__)

data = {
  "number": 0
}

@app.route("/contador", methods=['GET', 'POST', 'DELETE'])
def soma():
  if request.method == 'GET':
    return {"numero": data['number']}, 200
  elif request.method == 'POST':
    content = request.json
    data["number"] = int(content['numero'])
    return {"numero": data["number"]}, 200
  elif request.method == 'DELETE':
    data["number"] = 0
    return {"numero": data["number"]}, 202


@app.route("/contador/incrementa", methods=['PUT'])
def incrementa():
  data["number"] += 1
  return {"numero": data["number"]}, 202

if __name__ == "__main__":
  app.run(debug=True)