import time
from selenium import webdriver
import os
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import datetime
from random import randint
import json
from pymongo import MongoClient
import requests
import re
from bson import ObjectId
from pprint import pprint
from decimal import Decimal
def Start(token,navegador):
  site = 'https://www.terabyteshop.com.br/'
  # termo_pesquisa = 'Memoria RAM 8gb'
  termo_pesquisa = input('Termo de pesquisa:')
  estabelecimento = input('Estabelecimento:')
  categoria = input('Categoria:')


  if estabelecimento == '':
    estabelecimento =  '60d1250161605f061004cceb'
  if termo_pesquisa == '':
    termo_pesquisa =  'placa de video'
  print('estabelecimento selecionado:',estabelecimento)
  n_produt = input('Quantidade de produtos:')
  if n_produt != '':
    n_produt = int(n_produt)
  else:
    n_produt = 1

  navegador.get(site)
  campo_busca = WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.ID, 'isearch')))
  #navegador.find_element_by_id('misearch')
  campo_busca.send_keys(termo_pesquisa)
  campo_busca.send_keys(Keys.ENTER)
  time.sleep(3)
  p = 1
  print(f"Lendo página {p}...")
  html = navegador.find_element_by_id("prodarea")

  html = html.get_attribute("innerHTML")

  sopa = BeautifulSoup(html, 'lxml')
  #print('item count',len(sopa.find_all('div', {'class': 'commerce_columns_item_inner'})))
  for i in sopa.find_all('div', {'class': 'commerce_columns_item_inner'}):
    try:
      url = i.find('a', {'class': 'prod-name'}).attrs['href']
      navegador.get(url)
      preco = 0
      try:
        preco = navegador.find_element_by_id('valVista')
      except NoSuchElementException:
        alternativePreco = navegador.find_element_by_class_name('p3')
        preco = alternativePreco.find_element_by_tag_name('span')
        pass
      if p == 1:
        try:
        #  navegador.implicitly_wait(10)
         WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.ID,'btnCloseCookie'))).click()
        except TimeoutException:
          pass
      time.sleep(1)
      element = navegador.find_elements_by_class_name('panel-group')
      element[2].click()
      time.sleep(1)
      title = navegador.find_element_by_class_name('tit-prod')
      tecnica = navegador.find_element_by_class_name('tecnicas')
      esptecnica = tecnica.find_elements_by_tag_name('p')
      obj = {}
      obj['marca'] = ''
      obj['marca'] = ''
      obj['modelo'] = ''
      obj['nome'] = title.text
      precoPuro = preco.text.strip('R$').replace(' ', '')
      obj['preco'] = int(precoPuro.replace(',','').replace('.','')) / 100
     # a_string = a_string.replace(',',"")
    #  obj['preco'] = int(re.search(r'\d+', a_string).group()) / 100
      for f in esptecnica:
        split = f.text.split(':')
      if len(split) == 2:
        nome = split[0].replace('\r', '').replace('\n', '').lower()
        value = split[1].replace('\r', '').replace('\n', '').lower()
        obj[nome] = value
      finalObj = {
        'nome':obj['nome'],
        'fabricante':obj['marca'],
        'modelo':obj['modelo'],
        'preco':obj['preco'],
        'status':True,
        'estabelecimento':estabelecimento,
        'descricao':tecnica.get_attribute("innerHTML"),
        'categorias':[categoria]
      }
      headers = {
        'x-access-token': token,
       }
      requests.post('http://127.0.0.1:8000/v1/produto', json=finalObj, headers=headers)
      if p == n_produt:
        print("Extração concluída.")
        break
      p += 1
    except Exception:
      if p == n_produt:
        print("Extração concluída.")
      raise
    pass

    #   x = {"name":"teste"}
    #  // print(x['name'])
        # elif f.find_element_by_tag_name('p') is not None:
        #   item = f.find_element_by_tag_name('p')
        #   print(desc.text + " : " + item  + "\n")


      #print('esp',item.find('strong').text)
  # navegador.close()
