from flask import Flask, request

app = Flask(__name__)

@app.route("/soma", methods=['POST'])
def soma():
  content = request.json
  return {"resultado": int(content["x"]) + int(content["y"])}, 200

if __name__ == "__main__":
  app.run(debug=True)