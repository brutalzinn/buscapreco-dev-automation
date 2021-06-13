import sys
import os
from utils import user
def Start(tipo,navegador):
    navegador.get('http://painel.buscapreco.local/admin/loja')
    createButton = navegador.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/main/div[2]/div/div[1]/h6[2]/button/span[1]')
    createButton.click()
    cnpjLoja = navegador.find_element_by_xpath('//*[@id="cnpj"]')
    nomeLoja = navegador.find_element_by_xpath('//*[@id="nome"]')
    nomeLoja.send_keys(user.generate_name())
    cnpjLoja.send_keys(user.generate_cnpj())
