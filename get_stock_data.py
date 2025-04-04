from flask import Flask
from vnstock import stock_intraday_data
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def run():
    today = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%Y-%m-%d')
    symbols = ["HPG", "FPT", "VNM", "MWG", "FUEVFVND"]
    data = {}

    for symbol in symbols:
        try:
            df = stock_intraday_data(symbol, start_date=today, end_date=today, resolution=1)
            if not df.empty:
                latest = df.iloc[-1]
                data[symbol] = {
                    "price": latest["close"],
                    "time": latest["time"]
                }
        except Exception as e:
            data[symbol] = {"error": str(e)}

    webhook_url = "https://hook.us2.make.com/msge7hk1g1sg2o5fc1ctrz9gyfsj42ir"
    response = requests.post(webhook_url, json=data)
    return f"Sent to webhook: {response.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
