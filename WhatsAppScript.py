from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
def automate(client = "xyz",msg = "xyz",code = 0):
    if code == 1:
        
        driver.get("https://web.whatsapp.com/")
    #driver.maximize_window()
    #//span[@title="abc"]
    #//*[@id="main"]/footer/div[1]/div[2]
    if code == 2:
        user = driver.find_element_by_xpath("//span[@title='{}']".format(client))
        user.click()
        msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        for i in range(5):
            msg_box.send_keys(msg+str(i))
            #time.sleep(1)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
        
    
print("done")
