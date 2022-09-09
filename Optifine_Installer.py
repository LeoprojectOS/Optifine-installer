import pyautogui
import time
import wget
print('Inserisci il tuo username')
usr = input()
print('Inserisci la versione della optifine')
ver = input()
if str(ver) == '1.19.2':
    url = 'https://github.com/LeoprojectOS/Optifine-installer/raw/main/OptiFine_1.19.2_HD_U_H9.jar'
    
    wget.download(url, '/Users/'+usr+'/Documents')
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('cd C:\\Users\\'+usr+'\\Documents')
    pyautogui.press('enter')
    pyautogui.write('java -jar OptiFine_1.19.2_HD_U_H9.jar')
    pyautogui.press('tab')
    pyautogui.press('enter')
elif str(ver) == '1.18.2':
    url2 = 'https://github.com/LeoprojectOS/Optifine-installer/raw/main/OptiFine_1.18.2_HD_U_H7.jar'
    wget.download(url2, '/Users/'+usr+'/Documents')
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('cd C:\\Users\\'+usr+'\\Documents')
    pyautogui.press('enter')
    pyautogui.write('java -jar OptiFine_1.18.2_HD_U_H7.jar')
    pyautogui.press('tab')
    pyautogui.press('enter')
elif str(ver) == '1.17.1':
    url3 = 'https://github.com/LeoprojectOS/Optifine-installer/raw/main/OptiFine_1.17.1_HD_U_H1.jar'
    wget.download(url3, '/Users/'+usr+'/Documents')
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('cd C:\\Users\\'+usr+'\\Documents')
    pyautogui.press('enter')
    pyautogui.write('java -jar OptiFine_1.17.1_HD_U_H1.jar')
    pyautogui.press('tab')
    pyautogui.press('enter')
elif str(ver) == '1.16.5':
    url3 = 'https://github.com/LeoprojectOS/Optifine-installer/raw/main/OptiFine_1.16.5_HD_U_G8.jar'
    wget.download(url3, '/Users/'+usr+'/Documents')
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('cd C:\\Users\\'+usr+'\\Documents')
    pyautogui.press('enter')
    pyautogui.write('java -jar OptiFine_1.16.5_HD_U_G8.jar')
    pyautogui.press('tab')
    pyautogui.press('enter')
else:
    print('Versione non presente nel Repository')
    
    

