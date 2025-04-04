from flask import Flask
from get_stock_data import run

app = Flask(__name__)

@app.route("/")
def trigger():
    run()
    return "Stock data sent successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)