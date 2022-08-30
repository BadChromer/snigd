from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def main():
    driver.get('https://store.steampowered.com/account/notinterested/?p=2')
    login = driver.find_element_by_id('input_username')
    login.send_keys('login')
    password = driver.find_element_by_id('input_password')
    password.send_keys('password')

def log_in():    
    sign_in = driver.find_element_by_xpath('//*[@id="login_btn_signin"]/button')
    sign_in.click()
    two_factor = driver.find_element_by_id('twofactorcode_entry')
    two_factor.send_keys(input())
    submit = driver.find_element_by_xpath('//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]/div[1]')
    submit.click()

def wait_for_load():
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'ignored_app'))
        WebDriverWait(driver, 3).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

def delete_item():
    while True:
        remove = driver.find_element_by_class_name('remove')
        remove.click()
        driver.refresh()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    main()
    log_in()
    wait_for_load()
    delete_item()