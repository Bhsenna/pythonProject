from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Firefox()

navegador.get('https://externo.proway.com.br/login-aluno')
navegador.find_element('id', 'formLoginSubscriber_username').send_keys('bhsenna@gmail.com')
navegador.find_element('id', 'formLoginSubscriber_password').send_keys('24072005'+Keys.ENTER)
sleep(2)
navegador.find_element('xpath', '/html/body/div[1]/section/section/main/div/div/div/ul/li[1]/ul/li/button/span[2]').click()