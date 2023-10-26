import pyautogui
import time

usuario = 'bot'
senha = 'abc@12345'

def abrir_rms():
    path_rms = 'C:\\RMS\\WRMS\\SKY-SRVPRE-01\\PINHEIRO\\EXE\\WRMS.exe'
    pyautogui.press('win')
    pyautogui.write(path_rms)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(usuario)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(senha)
    pyautogui.press('enter')
    time.sleep(4)    

def abrir_programa():
        imagem1 = pyautogui.locateOnScreen('src/assets/recebimento.png', confidence=0.9, grayscale=True)
        x = imagem1.x
        y = imagem1.y
        print(x, y)
        print("deu bom!")
    
abrir_rms()
abrir_programa()