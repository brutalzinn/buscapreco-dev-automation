import sys
import os
from utils import user
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
def Start(tipo,navegador):
    navegador.get('http://painel.buscapreco.local/admin/loja')
    element = navegador.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/main/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[4]/button[2]')
    actions = ActionChains(navegador)
    actions.move_to_element(element).click().perform()
    time.sleep(3)
    navegador.find_element_by_id('word').send_keys("belezinha teste")

