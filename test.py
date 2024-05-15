from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://mir-rast.ru/')

search = browser.find_element(By.CSS_SELECTOR, '.orig')
search.send_keys('Актинидия')

button = browser.find_element(By.CSS_SELECTOR, '.promagnifier')
button.click()

try:
    assert 'promagnifier' in browser.page_source
    print('Все отлично')
except Exception as err:
    print('Что-то не так(')

browser.close()
