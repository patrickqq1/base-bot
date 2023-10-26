import pyautogui as bot
import time

usuario = 'bot'
senha = 'abc@12345'

def abrir_rms():
    path_rms = 'C:\\RMS\\WRMS\\SKY-SRVPRE-01\\PINHEIRO\\EXE\\WRMS.exe'
    bot.press('win')
    bot.write(path_rms)
    time.sleep(2)
    bot.press('enter')
    time.sleep(2)
    bot.write(usuario)
    time.sleep(1)
    bot.press('tab')
    time.sleep(1)
    bot.write(senha)
    bot.press('enter')
    time.sleep(4)    

def abrir_programa():
        imagem1 = bot.locateOnScreen('src/assets/recebimento.png', confidence=0.9, grayscale=True)
        x,y = bot.center(imagem1)
        print(x, y)
        print("deu bom!")
    
abrir_rms()
abrir_programa()