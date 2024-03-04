# projeto-pyautogui1
Mestres da Automação - Dev Aprender - Como movimentar e clicar com PyAutoGUI

# DESAFIO 1 
Crie um codigo que movimente o mouse até a posição do navegador onde esta aberto o jogo Doge Miner 2 
clique repetidas vezes para passar da primeira fase do jogo  

# Para achar uma posição utilize o MouseInfo 
1 - Abra o terminal ou prompt de comando.
2 - Certifique-se de ter instalado o Python em seu computador. Você pode verificar digitando "python-version" 
3 - Instale o Mouseinfo através do comando "pip install mouseinfo". Obs: Mac ou Linux "python3 -m mouseinfo"
4 - Acesso o python.exe através do comando "python" 
5 - Importe os argumentos do MouseInfo através dos comandos:
-> from mouse info import mouseInfo
-> mouseInfo 
# Obs: caso o segundo comando mouseInfo não abra utilize o comando: 
mouseinfo.MouseInfoWindow()

# Link jogo Dog Miner2 
https://www.crazygames.com/game/doge-miner-2?_gl=1*1505btp*_ga*MjEzNDE4ODkzNy4xNjkwMTI2MjMy*_ga_37GXT4VGQK*MTcwOTU3Nzc4Ny4xNDUuMS4xNzA5NTc4ODE1LjAuMC4w

Posicione o mouse no local que deseja clicar e capture a posição com MouseInfo atalho F6 para capturar 

# SCRIPT  app.py 
Este código Python utiliza a biblioteca PyAutoGUI para automatizar cliques do mouse em uma determinada posição na tela. 
import pyautogui: Isso importa a biblioteca PyAutoGUI, que permite automatizar ações do mouse e do teclado.

from time import sleep: Isso importa a função sleep do módulo time, que é usada para pausar a execução do programa por um determinado período de tempo.

pyautogui.moveTo(-933,427,duration=2): Isso move o cursor do mouse para a posição (-933, 427) na tela, com uma duração de 2 segundos. As coordenadas (x, y) representam a posição do cursor na tela, onde (0, 0) é o canto superior esquerdo da tela.

for i in range(300):: Isso inicia um loop for que será executado 300 vezes.

sleep(0.1): Isso pausa a execução do programa por 0.1 segundos. Isso é feito para garantir que o programa não clique muito rapidamente, o que pode ser indesejável.

pyautogui.click(): Isso simula um clique do mouse na posição atual do cursor. Como o cursor foi movido para a posição (-933, 427) na tela anteriormente, isso fará com que o programa clique nessa posição.