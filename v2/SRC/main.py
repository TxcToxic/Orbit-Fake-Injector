import os
import time
import psutil
import sys
import webbrowser


def sPrint(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.1)


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


gtaRunning = False
os.system('title Orbit')
time.sleep(2.5)
print(r''' _____          __          __
/\  __`\       /\ \      __/\ \__
\ \ \/\ \  _ __\ \ \____/\_\ \ ,_\
 \ \ \ \ \/\`'__\ \ '__`\/\ \ \ \/
  \ \ \_\ \ \ \/ \ \ \L\ \ \ \ \ \_
   \ \_____\ \_\  \ \_,__/\ \_\ \__\
    \/_____/\/_/   \/___/  \/_/\/__/
''')
print('Using saved login.')
time.sleep(2)
print('{"version":1651257971}Saved configuration.')
time.sleep(0.1)
sys.stdout.write("Waiting for GTA5.exe")
sys.stdout.flush()
while gtaRunning is False:
    if checkIfProcessRunning('gta5'):
        gtaRunning = True
    else:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.5)
time.sleep(2.8)
print()
sPrint(":kekw: this is fake!")
webbrowser.open(url="https://github.com/TxcToxic/Orbit-Fake-Injector#info--note", new=True)
while True:
    time.sleep(120)
