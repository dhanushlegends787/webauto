from selenium import webdriver
import time
driver = webdriver.Chrome()

with open("s02.txt","r") as f:
    link=f.readlines()


driver.get('http://www.pdisk.net/upload?type=url')
email = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[1]/span/input')
email.send_keys("dhanush544531@gmail.com")


password = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[2]/span/input')
password.send_keys("dhanush787")

submit = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[3]/button/span')
submit.click()

def uploadfile(s,e):
    v = 1
    for i in range(9):
        season = "Game Of Thrones S0{}E0{}".format(s,e)
        e = e + 1
        time.sleep(1)
        driver.get('http://www.pdisk.net/upload?type=url')
        upload = driver.find_element_by_xpath('//*[@id="control-hooks_fileUrl"]')
        uploadlink = link[0].strip()
        upload.send_keys(uploadlink)
        filename = driver.find_element_by_xpath('//*[@id="control-hooks_fileTitle"]')
        filename.send_keys(season)
        agreebutton = driver.find_element_by_xpath('//*[@id="control-hooks_checkTos"]')
        if v==1:
            time.sleep(2)
            nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
            nextbutton.click()
            nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
            nextbutton.click()
            nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
            nextbutton.click()
            nextbutton = driver.find_element_by_xpath('// *[ @ id = "app"] / section / div[2] / div / div[3]')
            nextbutton.click()
            time.sleep(2)
            agreebutton.click()
            v = 2

        uploadbutton = driver.find_element_by_xpath('//*[@id="control-hooks"]/div[5]/div/div/div/button/span')
        uploadbutton.click()
        time.sleep(3)
    e = 10
    season="Game Of Thrones S0{}E{}".format(s,e)
    time.sleep(1)
    driver.get('http://www.pdisk.net/upload?type=url')
    upload = driver.find_element_by_xpath('//*[@id="control-hooks_fileUrl"]')
    uploadlink = link[0].strip()
    upload.send_keys(uploadlink)
    filename = driver.find_element_by_xpath('//*[@id="control-hooks_fileTitle"]')
    filename.send_keys(season)
    agreebutton = driver.find_element_by_xpath('//*[@id="control-hooks_checkTos"]')
    uploadbutton = driver.find_element_by_xpath('//*[@id="control-hooks"]/div[5]/div/div/div/button/span')
    uploadbutton.click()
    time.sleep(3)
uploadfile(3,1)
