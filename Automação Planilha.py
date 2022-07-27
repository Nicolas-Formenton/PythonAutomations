import time
import pyautogui
import pyperclip
import pandas as pd

#Delay
pyautogui.PAUSE = 1

#Passo 1: Entrar no sistema
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")

#Copiar
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")

pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(3)

#Passo 2: Navegar no sistema e encontrar a base de dados
pyautogui.click(x=382, y=285, clicks=2)
time.sleep(2)

#Passo 3: Download da base de dados
time.sleep(2)
pyautogui.click(x=382, y=285, clicks=2)

time.sleep(1)
pyautogui.click(x=382, y=285)

time.sleep(3)
pyautogui.click(x=140, y=148)
pyautogui.click(x=252, y=418)
pyautogui.click(x=499, y=430)

time.sleep(2)
pyautogui.click(x=1265, y=735, clicks=2)

#Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
tabela = pd.read_excel(r"C:\Users\Nicolas\Downloads\Vendas - Dez.xlsx")
print(tabela)

quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
empresas = tabela["ID Loja"].value_counts(normalize=True).map("{:.2%}".format)

print(f'Produtos: {quantidade:,}')
print(f'R$: {faturamento:,.2f}')
print(f'Dominância das empresas: {empresas}')


#Passo 5: Entrar no email 
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(1)

#Passo 6: Mandar um email para a diretoria com os indicadores
#Clicar no botão +
pyautogui.click(x=128, y=196)
time.sleep(1)

#Escrever o destinatário
pyautogui.click(x=1542, y=527)
pyautogui.write("nformenton@gmail.com")
pyautogui.press("tab") #Selecionar o EMAIL

#Escrever o assunto
pyautogui.press("tab") #Ir para o campo do ASSUNTO
pyperclip.copy("Relatório de Vendas") #Nome do assunto
pyautogui.hotkey("ctrl", "v") #Colar o assunto
pyautogui.press("tab") #Ir para o corpo do email

#Escrever o corpo do email
texto = f"""
Bom dia!

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos vendidos foi: {quantidade:,}
Dominância das Empresas: 
{empresas}

Abs,
Nicolas."""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

#Clicar no botão de Enviar
""" pyautogui.click(x=1308, y=1052) """
#ou
pyautogui.hotkey("ctrl", "enter")