//C++
//

const int sensorpin = A0;
const int sensorpower = 8;
const int RedLED = 2;
const int YellowLED = 3;
const int BlueLED = 4;

int sensor;

const int delayTime = 1000;

int wet = 800;
int dry = 500;

void setup(){
  pinMode(BlueLED,OUTPUT);
  pinMode(YellowLED,OUTPUT);
  pinMode(RedLED,OUTPUT);
  pinMode(sensorpower,OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  digitalWrite(sensorpower,HIGH);
  delay(10);
  
  sensor = analogRead(sensorpin);
  digitalWrite(sensorpower,LOW);
  
  Serial.println(sensor);
  
  digitalWrite(BlueLED,LOW);
  digitalWrite(YellowLED,LOW);
  digitalWrite(RedLED,LOW);
  
  if(sensor>wet){
    digitalWrite(BlueLED,HIGH);
  }
  else if(sensor<dry){
    digitalWrite(RedLED,HIGH);
  }
  else{
    digitalWrite(YellowLED,HIGH);
  }
  delay(delayTime);
}