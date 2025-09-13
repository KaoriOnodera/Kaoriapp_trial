import streamlit as st
import requests
from datetime import datetime
import pandas as pd

city_code_list = {
    "東京都":"130010",
    "大阪":"270000"
}

st.title("天気アプリ")
st.write("調べたい地域を選んでください。")

city_code_index = st.selectbox("地域を選んでください。",city_code_list.keys())
city_code = city_code_list[city_code_index]

current_city_code = st.empty()
current_city_code.write("選択中の地域" + city_code_index)

url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code

response = requests.get(url)

weather_json = response.json()
now_hour = datetime.now().hour

weather_now = "情報なし" 

if 0 <=now_hour and now_hour < 6:
    weather_now = weather_json['forecasts'][0]['chanceOfRain'].get('T00_06',"情報なし")
elif 6 <= now_hour and now_hour < 12:
    weather_now = weather_json['forecasts'][0]['chanceOfRain'].get('T06_12',"情報なし")
elif 12 <= now_hour and now_hour < 18:
    weather_now = weather_json['forecasts'][0]['chanceOfRain'].get('T12_18',"情報なし")
elif 18 <= now_hour and now_hour < 24:
    weather_now = weather_json['forecasts'][0]['chanceOfRain'].get('T18_24',"情報なし")

weather_now_text = "現在の降水確率：" + weather_now
st.write(weather_now_text)

df1 = pd.DataFrame(weather_json['forecasts'][0]['chanceOfRain'],index=["今日"])
df2 = pd.DataFrame(weather_json['forecasts'][1]['chanceOfRain'],index=["明日"])
df3 = pd.DataFrame(weather_json['forecasts'][2]['chanceOfRain'],index=["今日"])

df = pd.concat([df1,df2,df3])
st.dataframe(df)