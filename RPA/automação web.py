from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox()

navegador.get('https://www.google.com.br/')
navegador.find_element('name', 'q').send_keys('Senac'+Keys.ENTER)