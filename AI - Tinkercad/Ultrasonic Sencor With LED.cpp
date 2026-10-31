//C++
// 

int trigPin = 7;
int echoPin = 6;
int ledPin = 8;
long time;
float distance;

void setup()
{
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    time = pulseIn(echoPin, HIGH);
    Serial.print("Time : ");
    Serial.println(time);

    distance = time*0.0343/2;

    if(distance < 48){
        digitalWrite(ledPin, HIGH);
    }
    else{
        digitalWrite(ledPin, LOW);
    }

    Serial.print("Distance : ");
    Serial.println(distance);
}
