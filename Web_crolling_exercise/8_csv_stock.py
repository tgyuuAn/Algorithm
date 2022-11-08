import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액1-200.csv"
f=open(filename,"w",encoding="utf-8-sig", newline="") # newline이 없으면 리스트와 리스트 사이에 공백 줄이 2개가 된다.
writer=csv.writer(f)
writer.writerow("N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split())

for i in range(1,5):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={i}"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns= row.find_all("td")
        if len(columns)<=1:  # 필요없는 데이터는 스킵한다.
            continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)