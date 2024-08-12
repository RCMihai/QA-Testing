from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class Login():
    def loginTest(self):
        print("Incep testarea")
        #driver = webdriver.Chrome("...\\chromedriver.exe")
        #driver = webdriver.Firefox(executable_path = "E:\\ITSchool\\curs_2023\\curs17\\Login\\geckodriver.exe")
        driver = webdriver.Edge("E:\\ITSchool\\curs_2023\\curs17\\Login\\edgedriver_win32\\msedgedriver.exe")
        driver.get("https://www.demo.guru99.com/V4/")
        
        time.sleep(10)
        
        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        
        time.sleep(10)
        
        userName = driver.find_element(By.NAME, "uid")
        #userName = driver.find_element(By.XPATH,"//input[@name='uid']")
        userName.send_keys("mngr503832")
        
        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys("YzYdevy")
        
        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()
        
        actualTitle = driver.title
        
        assert actualTitle == "Guru99 Bank Manager HomePage", "FAILED actual title"
                
        
        time.sleep(10)
        
        driver.close()
        
    def loginTestUserNOK(self):
        print("Incep testarea")
        #driver = webdriver.Chrome("...\\chromedriver.exe")
        #driver = webdriver.Firefox(executable_path = "E:\\ITSchool\\curs_2023\\curs17\\Login\\geckodriver.exe")
        driver = webdriver.Edge("E:\\ITSchool\\curs_2023\\curs17\\Login\\edgedriver_win32\\msedgedriver.exe")
        driver.get("https://www.demo.guru99.com/V4/")
        
        time.sleep(10)
        
        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        
        time.sleep(10)
        
        userName = driver.find_element(By.NAME, "uid")
        #userName = driver.find_element(By.XPATH,"//input[@name='uid']")
        userName.send_keys("userNOK")
        
        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys("YzYdevy")
        
        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()
        
        test = 0
        try:
            actualTitle = driver.title
        except:
            print("Test Case PASSED")
            test = 1
            
        assert test == 1, "Test failed should not login"
            
        time.sleep(10)
        
        driver.close()
    
    def loginTestPasswordNOK(self):
        pass
    
    def loginTestUserAndPasswordNOK(self):
        pass
    
    def loginTestEmptyUser(self):
        pass
    
    def loginTestEmptyPassword(self):
        pass
    
        
    

logintest = Login()
#logintest.loginTest()
logintest.loginTestUserNOK()
#logintest.loginTestPasswordNOK()