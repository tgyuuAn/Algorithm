import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
#header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36""}
res = requests.get(url) #url에있는 정보를 가져옴.
res.raise_for_status() #오류나면 코드 멈춤.

soup = BeautifulSoup(res.text,"lxml")

#print(soup.a.attrs) # 속성을 딕셔너리 형태로 가져옴

#print(soup.a["href"]) # 딕셔너리에 key 값을 바로 넣어주면 그 value를 가져온다.
#print(soup.find("a", attrs={"class" : "Nbtn_upload"}).get_text()) # "a"태그에 해당하는 것 중 가장 처음에 만나는 정보 중 속성에 class : Nbtn_upload 인 것을 찾아준다.
#get_text() 는 텍스트만 가져옴.

cartoons = soup.find_all("a", attrs={"class" : "title"}) # 해당 하는 모든 정보를 list형태로 가져와 줌.
names = []
for cartoon in cartoons:
    url_2 = "https://comic.naver.com"+cartoon["href"]
    res_2 = requests.get(url_2)
    res_2.raise_for_status()
    soup_2 = BeautifulSoup(res_2.text,"lxml")
    print(soup_2.find("span", attrs={"class" : "wrt_nm"}).get_text().strip())