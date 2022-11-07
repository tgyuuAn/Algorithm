import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
 "Accept-Language" : "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"} #나라마다 다르게 표시되는 사이트, 쿠팡의 경우는 header에 이걸 쳐줘야함
res = requests.get(url, headers=headers, verify = False)
res.raise_for_status()
print(res.status_code) # 200이면 정상, 그 외에는 오류
print(requests.codes.ok) # 200을 뜻함.