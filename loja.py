import sys
import os
from utils import user
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
def Start(tipo,navegador):
    navegador.get('https://www.4devs.com.br/gerador_de_cep')
    generateCepButton = WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="btn_gerar_cep"]'))).click()
    cepGenerated = WebDriverWait(navegador, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#cep > span:nth-child(1)'))).text
    navegador.get('http://painel.buscapreco.local/admin/loja')
    WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/main/div[2]/div/div[1]/h6[2]/button/span[1]'))).click()
    WebDriverWait(navegador, 10).until(ec.presence_of_element_located((By.XPATH,'//*[@id="cep"]'))).send_keys(cepGenerated)
    time.sleep(2)
    WebDriverWait(navegador, 10).until(ec.presence_of_element_located((By.XPATH,'//*[@id="cnpj"]'))).send_keys(user.generate_cnpj())
    WebDriverWait(navegador, 10).until(ec.presence_of_element_located((By.XPATH,'//*[@id="nome"]'))).send_keys(user.generate_name())

