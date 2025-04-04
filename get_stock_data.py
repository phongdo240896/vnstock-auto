from vnstock import stock_intraday_data
import requests
from datetime import datetime

# Danh sách mã cần lấy giá
symbols = ["HPG", "FPT", "VNM", "MWG", "FUEVFVND"]

# Dữ liệu kết quả
data = {}

# Lấy giá gần nhất hôm nay (với khoảng thời gian từ 09:00 đến 15:00)
for symbol in symbols:
    try:
        df = stock_intraday_data(symbol, start_date="2024-04-04", end_date="2024-04-04", resolution=1)
        if not df.empty:
            latest = df.iloc[-1]
            data[symbol] = {
                "price": latest["close"],
                "time": latest["time"]
            }
    except Exception as e:
        data[symbol] = {"error": str(e)}

# Gửi kết quả về webhook của Make
webhook_url = "https://hook.us2.make.com/msge7hk1g1sg2o5fc1ctrz9gyfsj42ir"  # 👈 Anh thay bằng webhook thật

# Gửi
response = requests.post(webhook_url, json=data)
print(response.status_code, response.text)
