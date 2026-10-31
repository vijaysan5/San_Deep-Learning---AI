//C++
// 

int trigPin = 7;
int echoPin = 6;
int RLED = 2;
int YLED = 3;
int GLED = 4;
int Piezo = 5;
long time;
float distance;

void setup()
{
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
  pinMode(RLED,OUTPUT);
  pinMode(YLED,OUTPUT);
  pinMode(GLED,OUTPUT);
  pinMode(Piezo,OUTPUT);
  
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  time = pulseIn(echoPin, HIGH);
  Serial.print("Time : ");
  Serial.println(time);

  distance = time*0.0343/2;
  
  digitalWrite(RLED,LOW);
  digitalWrite(YLED,LOW);
  digitalWrite(GLED,LOW);
  digitalWrite(Piezo,LOW);
  
  
  if(distance > 100){
    digitalWrite(GLED,HIGH);
  }
  else if (distance < 50) {
    digitalWrite(RLED,HIGH);
    digitalWrite(Piezo,HIGH);
  }
  else{
    digitalWrite(YLED,HIGH);
  }
  
  Serial.print("Distance : ");
  Serial.println(distance);
}