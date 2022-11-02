from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  print("asldfa;lskdfj")
  return "Hello world"

if __name__ == '__main__':
  print("hello world!")
  app.run(host="0.0.0.0", port=8000, debug=True)