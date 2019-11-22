from selenium import webdriver
import time

#Load the driver for chrome and set the website
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.set_page_load_timeout("10")
driver.get("http://the-internet.herokuapp.com/")



def seleniumproject():

    try:
        #use element finder by link text to find key text
        javascript_alert = driver.find_element_by_link_text('JavaScript Alerts')
        javascript_alert.click() #click on text
        print("\n"+"Element Found"+"\n")
        driver.implicitly_wait(10) # seconds

        #use xpath to locate the keystring and find button
        js_confirm = driver.find_element_by_xpath('//*[@id="content"]/div/ul/li[2]/button')
        js_confirm.click() #button clicked
        print("Button Clicked"+"\n")
        driver.implicitly_wait(10) # seconds

        #Retrieve the message on the Alert window
        obj = driver.switch_to.alert
        message=obj.text
        print ("Popup: '"+ message + "' appeared"+"\n")

        #use accept() to accept the Alert message
        obj.accept()
        driver.implicitly_wait(10) # seconds

        #look for the result and return a print value for it
        Result = driver.find_element_by_id("result")
        print("Message appeared: " + Result.text+"\n")
        driver.implicitly_wait(10) # seconds

    except Exception as err:
        raise err

    finally:
        driver.close()

if __name__ == "__main__":
    seleniumproject()

