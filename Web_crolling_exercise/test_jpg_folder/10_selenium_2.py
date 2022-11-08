from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #BACKSPACE나 ENTER키 등 키보드 자판을 쓰게하는 함수
from selenium.webdriver.support.ui import WebDriverWait # time 모듈 없이 대기시간 주기위해 쓰는 함수
from selenium.webdriver.support import expected_conditions as EC # time 모듈 없이 대기시간 주기위해 쓰는 함수

browser = webdriver.Chrome("../chromedriver.exe")
browser.get("http://naver.com")
try:
    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,""))) #안에 요소를 얻을 때 까지 10초동안 기다림. 나오지 않으면 에러 발생
finally:
    browser.quit()