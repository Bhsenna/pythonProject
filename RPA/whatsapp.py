from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Firefox()

navegador.get('https://web.whatsapp.com/')
sleep(15)
navegador.find_element('xpath', '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys('Cauan'+Keys.ENTER)
sleep(1)
navegador.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').click()

mensagem = 'Hello There'
for i in mensagem:
    navegador.find_element('css selector', '[title="Mensagem"]').send_keys(i)
navegador.find_element('css selector', '[title="Mensagem"]').send_keys(Keys.ENTER)