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
