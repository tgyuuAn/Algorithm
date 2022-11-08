from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #BACKSPACE나 ENTER키 등 키보드 자판을 쓰게하는 함수
import time
import pyperclip # 네이버 로그인을 우회하기 위해 복사 - 붙여넣기 형식으로 ID와 PASSWORD를 넘겨줘야함
#그냥 생으로 입력할경우 네이버 자동입력에 탐지됨

#element 를 지우고싶으면 find_elemnt 한 다음 .clear() 사용
user_id=""
user_pw=""

browser = webdriver.Chrome("../chromedriver.exe") # 크롬드라이버 경로 설정
#browser.maxmize_window() #창 최대화로 실행
browser.get("http://naver.com")

browser.find_element(By.CLASS_NAME,"link_login").click()
pyperclip.copy(user_id)
browser.find_element(By.ID,"id").send_keys(Keys.CONTROL,"v")
time.sleep(1)
pyperclip.copy(user_pw)
browser.find_element(By.ID,"pw").send_keys(Keys.CONTROL,"v")
time.sleep(1)
browser.find_element(By.CLASS_NAME,"btn_login").click()

#browser.find_element(By.ID,"search_btn").click()
html = browser.page_source # 해당 페이지의 html을 가지고 온다. 이후 beautifulsoup 를 이용해서 크롤링.
print(html)

browser.quit()