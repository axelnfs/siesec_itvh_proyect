from asyncio import subprocess
import os
from datetime import datetime
import subprocess
# import pyautogui

def generarNombreRepoSQL():
    now = datetime.now()
    nowday = now.day
    nowmonth = now.month
    nowyear = now.year
    nowhour = now.hour
    nowminute = now.minute
    nowsecond = now.second
    nombreArchivo = "recovery-"+str(nowday)+"_"+str(nowmonth)+"_"+str(nowyear)+"_t-"+str(nowhour)+"-"+str(nowminute)+"-"+str(nowsecond)+".sql"
    return nombreArchivo

def navMySQLfolderBin():
    os.chdir("/home/InugamiKylo")
    print("la ruta es " + os.getcwd())

# def keypressenter():
#     time.sleep(2.0)
#     pyautogui.press('enter')

def generateRecovery():
    navMySQLfolderBin()
    os.system("mysqldump --user root --password=Lexa1990. --databases SieSecundaria > recovery/"+generarNombreRepoSQL())
    print("Terminado")

if __name__ == "__main__":
    generateRecovery()