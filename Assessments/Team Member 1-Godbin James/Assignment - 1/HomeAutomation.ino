// C++ code
//
#include<Servo.h>

#define echoPin 12
#define trigPin 3
long duration;
int distance;

Servo s;


int pirIn = 4;
int fanOut = 8;
int buzzOut = 13;
int lightOut = 2;
int nightLock = 7;

int ldrIn = A0;
int tempIn = A1;
int forceIn = A2;

int forceSt, tempSt, ldrSt, ultraSt, pirSt, lockSt, temp=0;
void setup()
{
  s.attach(5);

  pinMode(pirIn, INPUT);
  pinMode(echoPin,INPUT);
  pinMode(nightLock, INPUT);
  
  pinMode(buzzOut, OUTPUT);
  pinMode(trigPin,OUTPUT);
  pinMode(lightOut, OUTPUT);
  pinMode(fanOut, OUTPUT);
  Serial.begin(9600);
}
float getTemp()
{
    int reading = analogRead(tempIn);  
    float voltage = reading * 5.0;
    voltage /= 1024.0; 
    //Serial.print(voltage); Serial.println(" volts");
    float temperatureC = (voltage - 0.5) * 100 ;                                      
    //Serial.print(temperatureC); Serial.println(" degrees C"); 
    return temperatureC;
}
int getDistance()
{
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  
  duration=pulseIn(echoPin,HIGH);
  distance=(duration*0.034/2);
  return distance;
}
void alarm(int onOrOff)
{
  if(onOrOff)
  {
  	tone(13, 1000);
  	delay(1000);
  }
  else
  {  	
  	noTone(13);
  }
}

void openTheDoor()
{
  s.write(90);
  delay(1000);
}
void closeTheDoor()
{
  s.write(0);
  delay(1000);
}
void loop()
{
    pirSt = digitalRead(pirIn);
    ldrSt = analogRead(ldrIn);
    tempSt = getTemp();
    ultraSt = getDistance();
    lockSt = digitalRead(nightLock);
    forceSt = analogRead(forceIn);
  
    Serial.print("PIR = ");Serial.println(pirSt);
    Serial.print("ldrSt = ");Serial.println(ldrSt);
    Serial.print("tempSt = ");Serial.println(tempSt);
    Serial.print("ultraSt = ");Serial.println(ultraSt);
    Serial.print("lockSt = ");Serial.println(lockSt);
    Serial.print("forceSt = ");Serial.println(forceSt);
    Serial.print("temp = ");Serial.println(temp);
	if(ldrSt > 500)
	{
        //Human Entered the room and the room is dark so switch on the light
        if(pirSt == 1)
        	temp++;
      	if(ldrSt>= 500 && temp%2!= 0)
			digitalWrite(lightOut, HIGH);
        if(temp%2==0)
	        digitalWrite(lightOut, LOW);
	}
	if(tempSt > 25)
	{
		//if the temperature of the room is > 25*C then switching on the fan
		digitalWrite(fanOut, HIGH);
	}
    else
    {
      digitalWrite(fanOut, LOW);
    }
	if(ultraSt < 50)
	{
		//if the distance betweeen the human and the door is < 50 cm then the door automatically opened
		openTheDoor();
	}
	else
	{
		closeTheDoor();
	}

	if(lockSt == 1 && forceSt > 200)
	{
		//if nightLock is Switched on and burglar is detected by force sensor then alarm
		alarm(1);
	}
	else
	{
		alarm(0);
	}
    Serial.println("");
}



  