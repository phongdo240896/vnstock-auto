from vnstock import stock_historical_data
import requests
import datetime

# Cấu hình
symbol = "HPG"
today = datetime.datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# Lấy giá
data = stock_historical_data(symbol, start_date=yesterday, end_date=today, resolution='1D')
last_price = data.iloc[-1].to_dict()

# Gửi về Make (Thay webhook của anh vào dòng dưới)
requests.post(
    "https://hook.us2.make.com/msge7hk1g1sg2o5fc1ctrz9gyfsj42ir",
    json={"symbol": symbol, "price": last_price}
)
