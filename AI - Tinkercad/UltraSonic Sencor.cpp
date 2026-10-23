"Ultra Sonic Sencor"
//c++ code
//

int trigPin = 7;
int echoPin = 6;
long time;
float distance;

void setup()
{
    pinMode(trigPin, OUTPUT); //SET OUTPUT
    pinMode(echoPin, INPUT); //SET INPUT
    Serial.begin(9600); //FOR COMMUNICATION
}

void loop()
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(7, LOW);

    //Serial Monitoring Time :
    time=pulseIn(echoPin , HIGH);
    Serial.print("Time : ");
    Serial.println(time);

    //Convert >>> Time to Distance :
    distance = time * 0.0343/2;

    Serial.print("Distance : ");
    Serial.println(distance);
}





"Ultra Sonic Sencor >>> With LED Light"
//c++ code
//

int trigPin = 7;
int echoPin = 6;
int ledPin = 8;
long time;
float distance;

void setup()
{
    pinMode(trigPin, OUTPUT); //SET OUTPUT
    pinMode(echoPin, INPUT); //SET INPUT
  	pinMode(ledPin, OUTPUT); //SET LED OUTPUT
    Serial.begin(9600); //FOR COMMUNICATION
}

void loop()
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    //Serial Monitoring Time :
    time=pulseIn(echoPin , HIGH);
    Serial.print("Time : ");
    Serial.println(time);

    //Convert >>> Time to Distance :
    distance = time * 0.0343/2;

  if(distance<50){
    digitalWrite(ledPin, HIGH);
    delay(500);
  }
  else {
    digitalWrite(ledPin, LOW);
  }
  
    Serial.print("Distance : ");
    Serial.println(distance);
}