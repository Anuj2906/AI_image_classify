import bs4
from PIL import Image
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import requests
import os
import time


PATH = r"C:\Users\anujg\Downloads\Programs\chromedriver_win32\chromedriver.exe"
service = Service(PATH)
options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1920,10800")
# Made window size so much that 50 images can fit in one window so that all images will be loaded

driver = webdriver.Chrome(service=service, options=options)
# driver.get(urlW)
# os.makedirs('ai-generated-images')

def dloadimg(url, name):
    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join('resized',name+".jpg"), 'wb') as file:
            # # file = file.resize((400, 400))
            file.write(reponse.content)
            # try:
            #     image = Image.open(reponse.content)
            #     image = image.resize((400, 400))
            #     image.save(file)
            # except Exception as e:
            #     print(e)
            
def section_length(driver):
    fig_xpath = '//*[@id="main"]/div[3]/div/div[2]/section/figure'
    figures = driver.find_elements(by="xpath", value=fig_xpath)
    return len(figures)

def dload(urlW,name,pc):
        driver.get(urlW)
        num_img = section_length(driver)
        print(num_img)
        for i in range(1, num_img+1):
            ImageXPath = """//*[@id="main"]/div[3]/div/div[2]/section/figure[%s]/div/a/img"""%(i)
            # ImageElement = driver.find_element_by_xpath(ImageXPath)
            
            timeStarted = time.time()
            while True:
                try:
                    ImageElement = driver.find_element(by="xpath", value=ImageXPath)
                    ImageURL = ImageElement.get_attribute("src")
                    
                    if ImageURL == "https://freepik.cdnpk.net/img/1px.png":
                        currentTime = time.time()
                        if currentTime - timeStarted > 10:
                            print("Timeout! moving to next image")
                            break
                    elif ImageURL != "https://freepik.cdnpk.net/img/1px.png":
                        dloadimg(ImageURL, name+"_pg_no."+str(pc)+"img"+str(i))
                        print("Downloaded image no. %s of page no. %s." %(i,pc))
                        break
                    else:
                        break
                except:
                    print("Couldn't download an image %s, continuing downloading the next one"%(i))
                    break
        
pgcnt  = 1
while pgcnt<23:
    urlW = "https://www.freepik.com/photos/ai-generated/%s"%(pgcnt)
    dload(urlW,"AI_Img",pgcnt)
    pgcnt = pgcnt + 1
            



driver.close()