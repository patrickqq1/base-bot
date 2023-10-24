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
    mercadoria_check = pyautogui.locateOnScreen("./src/assets/mercadorias.png", confidence=0.9, grayscale=True)
    if mercadoria_check is not None:
        x = mercadoria_check.left + 20
        y = mercadoria_check.top + 10
        pyautogui.doubleClick(x, y)
        print("deu bom!")
    
abrir_rms()
abrir_programa()