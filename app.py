from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Study Buddy AI v1"

if __name__ == '__main__':
    app.run(debug=True)