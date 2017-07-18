import pyautogui, time, os

mc = pyautogui

mc.PAUSE = 0

mc.FAILSAFE = True

time.sleep(10)


'''
def bot():
    while True:        
        time.sleep(3)
        t = 0
        if t == 0:
            mc.typewrite("t!fish\n")
        elif t == 30:
            t = 0
        else:
            t += 1
'''

def chatspam():
    while True:
        time.sleep(2)
        mc.typewrite("ioandioa \n")
        
    
def fish():
    time.sleep(5)
    while True:
        mc.typewrite("t!fish\n")
        mc.typewrite("potato fishcake \n")
        time.sleep(1)
        mc.typewrite("almond cherries \n")
        time.sleep(1)
        mc.typewrite("chocolate steak \n")
        time.sleep(3)
        mc.typewrite("milk and cookies \n")
        time.sleep(3)
        mc.typewrite("t!fish sell garbage \n")
        time.sleep(3)
        mc.typewrite("t!fish sell common \n")
        time.sleep(3)
        mc.typewrite("t!fish sell uncommon \n")
        time.sleep(17)
        
