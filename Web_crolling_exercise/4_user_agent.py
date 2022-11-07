import requests
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
url = "https://blog.naver.com/tgyuu_"
res=requests.get(url, headers=headers)
print(res.status_code) # 200이면 정상, 그 외에는 오류
print(requests.codes.ok) # 200을 뜻함.
res.raise_for_status() # 200이면 코드 계속실행, 200이아니면 에러를 내고 멈춤
print("웹 스크래핑을 실시합니다.")

with open("naver.html","w", encoding="utf-8") as f:
    f.write(res.text)