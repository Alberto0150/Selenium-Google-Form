from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

option = webdriver.ChromeOptions()
# option.add_argument("-incognito") # Uncomment to open the chrome in incognito mode
option.add_experimental_option("excludeSwitches", ['enable-automation'])
# option.add_argument('log-level=3') # Uncomment to hide every type of warning message
option.add_argument("disable-infobars")
option.add_argument("--disable-extensions")
# option.add_argument("--headless") # Uncomment to make it run in background
# option.add_argument("start-maximized") # Uncomment to start in maximize window
# option.add_argument("disable-gpu") # Uncomment to disable GPU

# Change the Chrome Webdriver .exe location
browser = webdriver.Chrome(executable_path ='C:\\Users\\ASUS\\Downloads\\Chromium\\chromedriver.exe', options=option)

# Change the Google Form link
# browser.get("https://forms.gle/a4caUgZUmH341GX86") # example Google Form

# Textbox input with XPATH
textboxes = browser.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')

# Linear scale input with CSS Selector
linearscale_hal1_no1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_hal1_no2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div')  


time.sleep(2)

# Hit Time
textboxes.send_keys("Hello 1")

x = random.randrange(3,5)
print(x)
linearscale_hal1_no1.click()
linearscale_hal1_no1.send_keys(Keys.ARROW_DOWN * x)



x = random.randrange(4,5)
print(x)
linearscale_hal1_no2.click()
for _ in range(x):
    linearscale_hal1_no2.send_keys(Keys.ARROW_RIGHT)
    time.sleep(1)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span')  
nextbutton.click()

time.sleep(2)
# Setup page 2
# Radio button input with XPATH
pick = ['//*[@id="i5"]','//*[@id="i8"]','//*[@id="i11"]']
radiobuttons_hal2 = browser.find_element("xpath", random.choice(pick))
submitbutton = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')))

radiobuttons_hal2.click()
submitbutton.click()


browser.close()