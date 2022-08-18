# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup




class TestWebAutomation(object):
    
    
    def browser_cfg(self):
        chromedriver_path = chromedriver_autoinstaller.install("./")
        options =Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-infobars")
        if options.headless is True:
            print("Scraping on headless mode.")
            options.headless = True
        else:
            options.headless = False
        #options.add_argument("--no-sandbox")#Linux 必須加
        #options.add_argument("--disable-dev-shm-usage") #Linux 必須加
        
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        return driver
    def test_android_ver(self):
        android_url = "https://play.google.com/store/apps/details?id=com.bitoex.bitoproapp"
        run = TestWebAutomation()
        driver = run.browser_cfg()
        driver.get(android_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[1]/c-wiz[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/c-wiz[2]/div[1]/section[1]/header[1]/div[1]/div[2]/button[1]"))).click()
        sleep(1)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        Android_page = driver.page_source
        A_soup = BeautifulSoup(Android_page, "html.parser")
        A_soup.encoding = "utf-8"
        A_expatistan_table = A_soup.find("div", class_="reAt0")
        driver.quit()
         
        return str(A_expatistan_table.string)
    
    def test_ios_ver(self):
        IOS_Ver=""
        ios_url = "https://apps.apple.com/tw/app/bitopro/id1393007496"
        run = TestWebAutomation()
        driver = run.browser_cfg()
        driver.get(ios_url)
        ios_page = driver.page_source
        i_soup = BeautifulSoup(ios_page, "html.parser")
        i_soup.encoding = "utf-8"
        i_expatistan_table = i_soup.find_all("p")
        
        for data in  i_expatistan_table :
            if "版本" in data.text:
                IOS_Ver= data.text.split()[1]
                
        driver.quit()
        
        return IOS_Ver
if __name__ == "__main__":
    try : 
        run=TestWebAutomation()
        Android_Ver = run.test_android_ver()
        ios_Ver = run.test_ios_ver()
        if Android_Ver == ios_Ver : print("Google Play and App Store 兩者版本號一致")   
        else: print("Google Play and App Store 兩者版本號不一致")
        
    except Exception as ex:
        print(f"Error Msg :{ex}")
    
