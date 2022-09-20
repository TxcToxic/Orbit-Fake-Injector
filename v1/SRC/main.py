import os
import time
import psutil


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

gtaRunning = False
os.system('title Orbit(Fake by -TOXIC-)')
time.sleep(2.5)
print(r''' _____          __          __
/\  __`\       /\ \      __/\ \__
\ \ \/\ \  _ __\ \ \____/\_\ \ ,_\
 \ \ \ \ \/\`'__\ \ '__`\/\ \ \ \/
  \ \ \_\ \ \ \/ \ \ \L\ \ \ \ \ \_
   \ \_____\ \_\  \ \_,__/\ \_\ \__\
    \/_____/\/_/   \/___/  \/_/\/__/
    
Disclaimer: This is not The real Injector''')
print()
print('Using saved Login.')
time.sleep(3.6)
print('Saved configuration.')
time.sleep(0.5)
print('Waiting for GTA5.exe...')
while gtaRunning is False:
    if checkIfProcessRunning('gta5'):
        gtaRunning = True
    else:
        pass
time.sleep(5.2)
print('Not Injected cuz its fake!')
time.sleep(100)
