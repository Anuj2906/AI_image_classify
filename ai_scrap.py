import bs4
from PIL import Image
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import requests
import os
import time

urlW = "https://impossibleimages.ai/images/"
PATH = r"C:\Users\anujg\Downloads\Programs\chromedriver_win32\chromedriver.exe"
service = Service(PATH)
options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)
# driver.get(urlW)

# os.makedirs('ai-generated-images')
# time.sleep(2)
def dloadimg(url, name):
    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join('ai2',name+".jpg"), 'wb') as file:
            file.write(reponse.content)
            
def section_length(driver):
    fig_xpath = '//*[@id="page"]/main/section/div/div/div[2]/article'
    figures = driver.find_elements(by="xpath", value=fig_xpath)
    return len(figures)
            
def dload(urlW,name):
    driver.get(urlW)
    driver.find_element(by="id", value="CybotCookiebotDialogBodyLevelButtonAccept").click()
    for j in range(30):
        j = j + 1
        time.sleep(15)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    num_img = section_length(driver)
    print(num_img)
    for i in range(1, num_img+1):
        
        ImageXPath = """//*[@id="page"]/main/section/div/div/div[2]/article[%s]/div/img"""%(i)
        # ImageElement = driver.find_element_by_xpath(ImageXPath)
        ImageElement = driver.find_element(by="xpath", value=ImageXPath)
        ImageURL = ImageElement.get_attribute("src")
        print(ImageURL)
        try:
            dloadimg(ImageURL, name+str(i))
            print("Downloaded element %s out of %s total." % (i, num_img))
        except:
            print("Couldn't download an image %s, continuing downloading the next one"%(i))
            
dload(urlW,"AI_Img_imp")      

# time.sleep(100)
driver.close()
            
