#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define trigPin D1  // Pini za distance sensor
#define echoPin D2

#define turnTime 100 // Time to turn in ms.
 
const char* ssid = "DragonHack";
const char* password = "goodh4ck";

#define TEST_LED 16
 
void setup () {
   pinMode(trigPin, OUTPUT);  // Distance sensor setup
   pinMode(echoPin, INPUT);
  
   digitalWrite (trigPin, LOW);
  
 Serial.begin(115200);
 WiFi.begin(ssid, password);
 while (WiFi.status() != WL_CONNECTED) {
   delay(1000);
   Serial.print("Connecting..");
 }
 pinMode(D0, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
 digitalWrite(D0, HIGH);     // Initialize the LED_BUILTIN pin as an output 
 pinMode(D4, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
 digitalWrite(D4, HIGH);     // Initialize the LED_BUILTIN pin as an output
}
 
void loop() {
  HTTPClient http;  //Declare an object of class HTTPClient
  int left = 0;
  int right = 0;
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    http.begin("http://phoebe.tano.si:8080/api/robot/instructions");  //Specify request destination
    int httpCode = http.GET(); //Send the request
    if (httpCode > 0) { //Check the returning code
      String payload = http.getString();   //Get the request response payload
      Serial.println(payload);                     //Print the response payload
    } else {
      Serial.println("Error" + String(httpCode));  
    }
    http.end();   //Close connection
    delay(1000);
    //HTTPClient http;  //Declare an object of class HTTPClient
    String state = "running"; // or "stopped" or "rotating"
    http.begin("http://phoebe.tano.si:8080/api/robot/status?state=" + state + "&timestamp=" + String(millis()));  //Specify request destination
    httpCode = http.GET(); //Send the request

    digitalWrite(trigPin, HIGH);  // Read distance from distance sensor
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    float distance1 = pulseIn(echoPin, HIGH)/58.2; // Distance in cm

    if (distance < 20.0){
      // Send distance to server and start turn command
    }

    
    if (httpCode > 0) { //Check the returning code
      String payload = http.getString();   //Get the request response payload
      Serial.println(payload);                     //Print the response payload
    } else {
      Serial.println("Error" + String(httpCode));  
    }
    http.end();   //Close connection   
     
  } else {
    Serial.println("Not connected"); 
  }
  // Drive motor
}

void turn(void)
{
    analogWrite(enablePin2, tSpeed);
    digitalWrite(enablePin1, LOW);
    
    delay(turnTime);
}
