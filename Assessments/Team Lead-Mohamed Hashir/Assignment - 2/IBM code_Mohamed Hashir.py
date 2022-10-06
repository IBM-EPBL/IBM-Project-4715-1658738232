print(" IBM ASSIGNMENT - 2")

import random
import time
from time import sleep
c=0
while(True):
    temperature = random.randint(20,45)
    
    if(temperature<27):
        print("Temperature - ",temperature)
        print("temperature is low, make sure to get warm - *firewood starts to burn through IoT*")

    elif(temperature>38):
        print("Temperature - ",temperature)
        c=c+1
        if(c==5):
            print("Temperature - ",temperature)
            print("temperature is high, cool down kid - *AC gets turned ON*")
    
    humidity = random.randint(20,70)

    if(humidity<30):
        print("Humidity - ",humidity)
        print("Here drink water, stay hydrated")
    elif(humidity>50):
        print("Humidity - ",humidity)
        print("Should be cool, stay warm")
    sleep(1)
