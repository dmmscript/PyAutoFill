import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=684, y=407)
pyautogui.write("meuemail@email.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=837, y=568)
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

linha = 0
for linha in tabela.index:
    pyautogui.click(x=814, y=290)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str("obs"))
    pyautogui.press("tab")
 
    pyautogui.press("enter")
    pyautogui.scroll(100000)

