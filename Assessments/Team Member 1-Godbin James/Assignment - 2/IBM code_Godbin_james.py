import random
from time import sleep
'''

In this Application the temperature and humidity is continuously
monitored, 5 samples are taken then the max occuring temperature or humidity
is taken as the current temperature and humidity for consideration then
by classifiying those value as normal or abnormal appropirate messages
or alearted.......

'''
def fun(lst):
    d = {}
    new = 0
    old = 0
    val = 0
    for el in lst:
        new = lst.count(el)
        if new > old:
            old = new
            val = el
    return val

def alert(t_list, h_list):
    f = 0
    h = fun(h_list)
    t = fun(t_list)
    if t < 27 and t> 38:
        print("WARNING FIRE FIRE RUN.........")
        print("Temp : "< t)
        f = 1
    else:
        if h < 30:
            print("WARNING FIRE FIRE RUN.........")
        elif h > 50:
            print("no problem USE SWEATER")
        print("Humi : ", h)
        f = 1
    return f
            
    
t_list = []
h_list = []
while 1:
    t = random.randint(10, 50)
    t_list.append(t)
    h = random.randint(0, 100)
    h_list.append(h)
    if len(h_list) == 10:
        f = alert(t_list, h_list)
        t_list=[]
        h_list=[]
        if f == 0:
            print("ENJOY WORKING")
    sleep(0.2)
    
