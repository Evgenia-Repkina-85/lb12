from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get('https://mir-rast.ru/product-tag/german-roses/')

button = browser.find_element(By.CSS_SELECTOR, '.rastenija-na-shtambe')
button.click()

button1 = browser.find_element(By.CSS_SELECTOR, '.checkbox woof_color_term woof_color_term_6073')
button1.click()

button2 = browser.find_element(By.CSS_SELECTOR, '.woof_607_66411cf666a32')
button2.click()

try:
    assert 'promagnifier' in browser.page_source
    print('Все отлично')
except Exception as err:
    print('Что-то не так(')

browser.close()
