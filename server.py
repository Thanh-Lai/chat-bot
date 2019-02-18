from flask import Flask, render_template
app = Flask(__name__)
from app import respond_to_messages

@app.route('/')
def hello_world():
  return "hello word"

@app.route('/message', methods=['POST'])
def send_message(message):
  response = respond_to_messages(message)
  return response

if __name__ == '__main__':
  app.run(debug=True)
