from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

### Webdriver Configuration
option = webdriver.ChromeOptions()
# option.add_argument("-incognito") # Uncomment to open the chrome in incognito mode
option.add_experimental_option("excludeSwitches", ['enable-automation'])
# option.add_argument('log-level=3') # Uncomment to hide every type of warning message
option.add_argument("disable-infobars")
option.add_argument("--disable-extensions")
# option.add_argument("--headless") # Uncomment to make it run in background
# option.add_argument("start-maximized") # Uncomment to start in maximize window
# option.add_argument("disable-gpu") # Uncomment to disable GPU

### Change the Chrome Webdriver .exe location
path = 'C:\\Users\\ASUS\\Downloads\\Chromium\\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path, options=option)

### Change the Google Form link
GForm_link = "https://forms.gle/a4caUgZUmH341GX86" # example Google Form, replace with your Google Form
browser.get(GForm_link) 

### Web Input section
## Setup page 1
time.sleep(2)
# Textbox input with XPATH
textbox_Xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input' #Sample Xpath for textbox
textboxes = browser.find_element("xpath",textbox_Xpath)


# Linear scale input with CSS Selector
#! What we don't want : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div > div.vd3tt'
#! What we want       : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div'
linearscale_page_1_no_1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_page_1_no_2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

## Page 1 Value
text_value = 'hello number_' + str(random.randint(0,1000))
textboxes.send_keys(text_value)

x = random.randrange(3,5)
linearscale_page_1_no_1.click()
linearscale_page_1_no_1.send_keys(Keys.ARROW_DOWN * x)

x = random.randrange(2,4)
linearscale_page_1_no_2.click()
linearscale_page_1_no_2.send_keys(Keys.ARROW_RIGHT * x)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span')  
nextbutton.click()

## Setup page 2
time.sleep(2)
# Radio button input with XPATH
#! //*[@id="i5"]
pick = ['//*[@id="i5"]','//*[@id="i8"]','//*[@id="i11"]']
radiobuttons_page_2 = browser.find_element("xpath", random.choice(pick))


pick = ['//*[@id="i19"]','//*[@id="i22"]','//*[@id="i25"]','//*[@id="i28"]','//*[@id="i31"]']
checkbox_page_2_1 = browser.find_element("xpath", random.choice(pick))
checkbox_page_2_2 = browser.find_element("xpath", random.choice(pick))
checkbox_page_2_3 = browser.find_element("xpath", random.choice(pick))
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')  

# Reuse same 'next' button 
radiobuttons_page_2.click()
checkbox_page_2_1.click()
checkbox_page_2_2.click()
checkbox_page_2_3.click()
nextbutton.click()

## Setup page 3
# Dropdown pick using XPATH [Coming Soon]
# value = ['Option 1','Option 2','Option 3']
# dropdown_xpath ='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div'
# dropdown_value = random.choice(value)
# dropdown = browser.find_element(By.XPATH,dropdown_xpath).click()
# dropdown.find_elements_by_tag_name(dropdown_value)

submitbutton = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')))
submitbutton.click()

# Close the browser
browser.close()