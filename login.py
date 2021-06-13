def Start(tipo,navegador):
   navegador.get('http://painel.buscapreco.local/')
   email = navegador.find_element_by_xpath('//*[@id="email"]')
   senha = navegador.find_element_by_xpath('//*[@id="senha"]')
   loginButton = navegador.find_element_by_xpath('/html/body/div/div[2]/main/div/form/button/span[1]')
   if tipo == 'admin':
      email.send_keys("admin@example.com")
   elif tipo == 'client':
      email.send_keys("client@example.com")
   elif tipo == 'user':
      email.send_keys("user@example.com")

   senha.send_keys("123")
   loginButton.click()