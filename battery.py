import os
from time import sleep
switch = 0
while True:
    os.system("acpi -V |egrep 'charg'> .txt")
    with open('.txt', 'r') as myfile:
        line=myfile.read().replace('\n', '')
    t = line.index("%")   
    try:
      f = float(line[t-3:t])
    except ValueError:
      f = float(line[t-2:t])
    
    pri  = 'Your laptop charge is less than %d percentage, Please plug the charger'%f
    pri1 = 'Battery charge is critically low, system is going for hibernation'
    pri2 = 'Battery fully charged'

    if 'Discharging' in line:
      if f < 15. :
        if f < 5:
          os.system("beep -f 1500 -l 80 -r 10")
          os.system("echo %s | festival --tts --pipe"%pri1)
          sleep(30)
           
        elif switch == 0:
         os.system("beep -f 1000 -l 700")
         os.system("echo %s | festival --tts --pipe"%pri)
         os.system("beep -f 1500 -l 100")
         switch = 1
    elif f > 99:
         os.system("echo %s | festival --tts --pipe"%pri2)       
         os.system("beep -f 900 -l 60 -r 15") 
         switch = 0     
         sleep(30)



