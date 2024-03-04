import pyautogui
from time import sleep

# Posição algo - use o mouseinfor
# Fazer algo com essa posição 
pyautogui.moveTo(-933,427,duration=2)
for i in range(300):
    sleep(0.1)
    pyautogui.click()