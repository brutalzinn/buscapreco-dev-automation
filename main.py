import importlib
import os
import sys
from selenium import webdriver
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
navegador = webdriver.Firefox(firefox_profile=firefox_profile,executable_path=os.path.join(sys.path[0], "geckodriver"))

#tipo = sys.argv[1]
print("Digite 1 - Para efetuar login no painel.")
print("Digite 2 - Para criar uma loja aleatória.")
print("Digite 3 - Para testar o sistema de confirmação.")
print("Digite 4 - Para gerar produtos reais em uma loja.")

entrada = input('Procedimento:')
tipo = input('Tipo de usuário:')

if entrada == '1':
  moduleAuto = importlib.import_module("login")
elif entrada == '2':
  moduleAuto = importlib.import_module("login")
  ds = getattr(moduleAuto, "Start")
  ds(tipo,navegador)
  moduleAuto = importlib.import_module("loja")
  ds = getattr(moduleAuto, "Start")
  ds(tipo,navegador)
elif entrada == '3':
  moduleAuto = importlib.import_module("login")
  ds = getattr(moduleAuto, "Start")
  ds(tipo,navegador)
  moduleAuto = importlib.import_module("loja_delete")
  ds = getattr(moduleAuto, "Start")
  ds(tipo,navegador)
elif entrada == '4':
  moduleAuto = importlib.import_module("request")
  token = getattr(moduleAuto, "loginAuth")
  produtoAuto = importlib.import_module("produto")
  ds = getattr(produtoAuto, "Start")
  ds(token(),navegador)