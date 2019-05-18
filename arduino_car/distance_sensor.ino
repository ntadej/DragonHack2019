const int trigPin = 11;  // Spremenljivke za distance sensor
const int echoPin = 12;

void setup() {
   pinMode(trigPin, OUTPUT);
   pinMode(echoPin, INPUT);
  
   digitalWrite (trigPin, LOW);
   Serial.begin(9600);
}

void loop() {
   digitalWrite(trigPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(trigPin, LOW);

   float distance = pulseIn(echoPin, HIGH)/58.2; // Distance in cm
   Serial.println(distance);
   delay(100);
}
