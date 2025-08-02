from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_ai():
    return 'Hello, AI!'

if __name__ == '__main__':
    app.run(debug=True)
