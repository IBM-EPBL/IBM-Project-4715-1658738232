import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
organization = "w63fd1"
deviceType = "JehoNi"
deviceId = "123"
authMethod = "token"
authToken = "12345678"

# Initialize GPIO


def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="lighton":
        print ("led is on")
    else :
        print ("led is off")
   
    #print(cmd)
    
        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        time.sleep(10)
        garbageLevel1=random.randint(0,100)
        garbageLevel2=random.randint(0,100)
        garbageLevel3=random.randint(0,100)
        garbageLevel4=random.randint(0,100)
        garbageLevel5=random.randint(0,100)
        
        data = { 'garbageLevel1' : garbageLevel1, 'garbageLevel2': garbageLevel2, 'garbageLevel3' : garbageLevel3, 'garbageLevel4': garbageLevel4, 'garbageLevel5':garbageLevel5}
        #}
        #print data
        def myOnPublishCallback():
            print (data)

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(4)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
