import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import DesiredCapabilities
PATH='C:\Coding_projects\selenium and chromedriver\chromedriver.exe'
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver=webdriver.Chrome(PATH,options=options)
def ouedkniss_renewer():
        driver.get('https://www.ouedkniss.com/')
        connect_button=driver.find_element_by_id('menu_seconnecter')   
        connect_button.click()
        username_form=driver.find_element_by_name('username')
        username_form.click()
        username_form.send_keys('WasMaestro')

        password_form=driver.find_element_by_name('password')
        password_form.click()
        password_form.send_keys('')

        connect_button2=driver.find_element_by_id('login_button')
        connect_button2.click()

        my_announcements=driver.find_element_by_xpath('//*[@id="button_annonces"]/a[2]')
        my_announcements.click()
        renew_button=driver.find_element_by_xpath('//*[@id="page"]/form/div[2]/div[4]/a[3]')
        renew_button.click()
        ok_button=driver.find_element_by_xpath('//*[@id="message_box_0"]/div/div/a[1]')
        ok_button.click()

        time.sleep(200)
ouedkniss_renewer()
