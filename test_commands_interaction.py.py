import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://saucedemo.com')

#find_element()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# click()
username.send_keys("standard_user")
password.send_keys("secret_sauce")
btn_login.click()
time.sleep(2)

# text
products = browser.find_element(By.XPATH,"//span[@class = 'title']")
print(products.text)
assert products.text.capitalize() == "Products"

#O XPATH abaixo [1] mapeia o primeiro indice da classe inventory_item_img, necessário () antes dos parâmetros de mapeamento
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
#A variável abaixo recebe o atributo alt para identificar e printar o texto
print(img_backpack.get_attribute("alt"))
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack"

open_menu_lateral = browser.find_element(By.ID, "react-burger-menu-btn")
open_menu_lateral.click()
time.sleep(2)
btn_logout = browser.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
btn_logout.click()
time.sleep(2)

quit()
# text

# send_keys()
# get_attribute()

