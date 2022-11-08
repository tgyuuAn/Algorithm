import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
 "Accept-Language" : "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
image_url = []

for i in range(2015,2022):
    url = f"https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    images=soup.find_all("img",attrs={"class":"thumb_img", "width":"116", "height":"164"})
    texts=soup.find_all("a",attrs={"class":"tit_main"})

    for idx in range(len(images)):
        print(texts[idx].get_text())
        image_url.append(images[idx]["src"])


print(f"다운로드할 이미지 개수 : {len(image_url)}개 입니다.")

while True:
    try:
        answer = input("저장하시겠습니까? 1.YES 2.NO")
        if answer == "1":
            for image in image_url:
                image_res=requests.get(image,headers=headers) # 이미지를 저장하려면 이미지를 따로 url로 따온 뒤,
                image_res.raise_for_status() # requests에 또 넣어야함.
                with open(fr"C:\Users\atg06\.vscode\파이썬2\Web_crolling_exercise\test_jpg_folder\{texts[idx].get_text()}.jpg","wb") as f: # 바이너리 쓰기형식으로 선언 후,
                    f.write(image_res.content) # content를 이용하여 저장.
        elif answer == "2":
            break
        else:
            raise Exception("\n정확한 값을 입력해주세요.")
    except:
        pass
    else:
        print("\n\n이미지 저장을 완료하였습니다.")
    finally:
        print("\n\nbreak")