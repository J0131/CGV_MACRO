from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import webbrowser
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from tkinter import *

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

send_id = "iwhy1201"
send_password = "hy0131!!"

window = Tk()

print("--------------- Start Macro ---------------")


def refersh():
    driver.refresh()
    driver.implicitly_wait(15)

    # move to iframe
    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/iframe"))

    # select mov
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[1]/\
                        div[1]/div[2]/div/div[3]/ul/li[2]/a').send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    time.sleep(0.5)

    # select region
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/\
                        div[1]/div[2]/div[2]/div/div[2]/div[1]/ul/li[9]').click()
    driver.implicitly_wait(15)
    time.sleep(0.5)

    # select detail region
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[1]/\
                        div[2]/div[2]/div/div[2]/div[1]/ul/li[9]/div/ul/li[11]').click()
    driver.implicitly_wait(15)
    time.sleep(0.5)
        
    # select date
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/\
                        div[1]/div[3]/div[2]/div/ul/div/li[4]/a').send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    time.sleep(0.5)


# webdriver 파일의 경로 입력
# 같은 디렉토리에 있기 때문에 chromedriver.exe파일 이름만 써줌
driver = webdriver.Chrome("chromedriver")

# 이동을 원하는 페이지 주소 입력
driver.get('https://www.cgv.co.kr/user/login/?returnURL=https%3a%2f%2fwww.cgv.co.kr%2fdefault.aspx')
driver.implicitly_wait(15)

# id 입력
id = driver.find_element(By.ID, 'txtUserId')
id.clear()
id.send_keys(send_id)
driver.implicitly_wait(15)
time.sleep(1)

# password 입력
pw = driver.find_element(By.ID, 'txtPassword')
pw.clear()
pw.send_keys(send_password)
driver.implicitly_wait(15)
time.sleep(1)

# click login 버튼
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/\
                    div/div[1]/div/form/fieldset/button').send_keys(Keys.ENTER)
driver.implicitly_wait(15)
time.sleep(1)

# 이동을 원하는 페이지 주소 입력
driver.get('http://www.cgv.co.kr/ticket/')
driver.implicitly_wait(15)

# move to iframe
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/iframe"))

# select mov
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[1]/\
                    div[1]/div[2]/div/div[3]/ul/li[2]/a').send_keys(Keys.ENTER)
driver.implicitly_wait(15)
time.sleep(1)

# select region
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/\
                    div[1]/div[2]/div[2]/div/div[2]/div[1]/ul/li[9]').click()
driver.implicitly_wait(15)
time.sleep(1)

# select detail region
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[1]/\
                    div[2]/div[2]/div/div[2]/div[1]/ul/li[9]/div/ul/li[11]').click()
driver.implicitly_wait(15)
time.sleep(1)
    
# select date
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/\
                    div[1]/div[3]/div[2]/div/ul/div/li[4]/a').send_keys(Keys.ENTER)
driver.implicitly_wait(15)

while True:
    # select mov time
    # driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/\
    #                 div[1]/div[4]/div[2]/div[3]/div[1]/div/ul/li[3]/a').send_keys(Keys.ENTER)
    # driver.implicitly_wait(15)
    # time.sleep(1)
    refersh()

    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/\
                        div[1]/div[3]/div[2]/div/ul/div/li[4]').click()
    driver.implicitly_wait(5)
    time.sleep(0.5)

    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/a[2]').send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    time.sleep(0.5)

    try:
        result=driver.switch_to.alert.accept()
        driver.implicitly_wait(15)
        time.sleep(0.1)
    except:
        # 동의
        driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/a').send_keys(Keys.ENTER)
        driver.implicitly_wait(15)

        driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[2]/\
                            div[1]/div[2]/div[1]/div[1]/div/div/div[3]/ul/li[2]/a').send_keys(Keys.ENTER)
        driver.implicitly_wait(5)
        
        group = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/\
                                     div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/a")
        print(group)

        group2 = driver.find_element(By.ID,"seats_list")
        print(group2)

        seat_list = group2.find_elements(By.CLASS_NAME, 'seat')
        print(len(seat_list))

        reserved = group2.find_elements(By.CLASS_NAME, "reserved")
        handicap = group2.find_elements(By.CLASS_NAME,"handicap")

        reserved.extend(handicap)

        possible_seat_list = []

        for i in seat_list:
            if i not in reserved:
                possible_seat_list.append(i)

        print(len(possible_seat_list))

        #possible_seat_list.reverse()

        for i in possible_seat_list:

            i.click()
            driver.implicitly_wait(15)

            driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/a[2]').send_keys(Keys.ENTER)
            driver.implicitly_wait(15)

            messagebox.showinfo("알림","알림")

            break
        
        driver.find_element(By.ID,'last_pay_radio3').send_keys(Keys.ENTER)
        driver.implicitly_wait(5)

        driver.find_element(By.ID,'tnb_step_btn_right').click()
        driver.implicitly_wait(5)

        while True:
            time.sleep(1)

        break

    time.sleep(0.2)