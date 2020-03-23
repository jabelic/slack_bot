import requests
from bs4 import BeautifulSoup

def weather():
    url = "https://weather.yahoo.co.jp/weather/jp/14/4610.html"
    # 横浜東部

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    # 1つ目の天気(つまり当日)だけを取得すればいいので、先頭を取得するだけである。
    weather = soup.find("p", class_ = "pict")
    #print(weather.getText())
    return weather.getText()

if __name__=="__main__":
    weather()


# import lxml.html
# html = lxml.html.fromstring(r.text)
# elems = html.findall()

