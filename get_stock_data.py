from vnstock import get_price_data
import requests
from datetime import datetime
import json

# Tạo ngày hôm nay dạng yyyy-mm-dd
today = datetime.now().strftime('%Y-%m-%d')

# Gọi API lấy dữ liệu giá ngày hôm nay cho mã HPG
data = get_price_data(
    symbol='HPG',
    resolution='1D',
    start_date=today,
    end_date=today
)

# Địa chỉ webhook Make.com của anh
webhook_url = "https://hook.us2.make.com/msge7hk1g1sg2o5fc1ctrz9gyfsj42ir"

# Gửi dữ liệu JSON về Make
response = requests.post(webhook_url, json={"symbol": "HPG", "date": today, "data": data})

# In trạng thái phản hồi từ webhook (debug)
print("Status:", response.status_code)
print("Response:", response.text)
