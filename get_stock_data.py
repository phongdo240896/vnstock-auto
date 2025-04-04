from vnstock import stock_intraday_data
import requests
from datetime import datetime
import pytz

# Lấy ngày hôm nay theo múi giờ Việt Nam
today = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%Y-%m-%d')

# Danh sách mã cổ phiếu cần lấy
symbols = ["HPG", "FPT", "VNM", "MWG", "FUEVFVND"]

# Dữ liệu kết quả
data = {}

# Lấy giá gần nhất trong hôm nay
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

# Gửi kết quả về webhook của Make
webhook_url = "https://hook.us2.make.com/msge7hk1g1sg2o5fc1ctrz9gyfsj42ir"  # Webhook thật của anh
response = requests.post(webhook_url, json=data)
print(response.status_code, response.text)
