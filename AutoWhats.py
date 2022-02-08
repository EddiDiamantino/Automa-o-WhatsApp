import pandas as pd

contatos = pd.read_excel('Contatos.xlsx')
display(contatos)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome()
navegador.get(" https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, 'Pessoa']
    numero = contatos.loc[i, 'Telefone']
    texto = urllib.parse.quote(f' Oiee {pessoa}, tudo bem?? {mensagem} https://forms.gle/UZx3qvtd1Aas1EDw8 ♥♥  ')
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
    time.sleep(10)
    #navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')[0].send_keys(Keys.ENTER)
    time.sleep(10)
