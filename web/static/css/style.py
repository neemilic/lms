from flask import Flask

app = Flask(__name__)
@app.route('/index')
def index():
    return """h1 {
   color: #d22e3a;
	 text-align: center;
}
img {
    margin-left: auto;
    margin-right: auto;
    max-width: 450px;
    background-color: #ffcc00;
    border: 1px solid gray;
    border-radius: 5px;
    padding: 10px;
}
"""
