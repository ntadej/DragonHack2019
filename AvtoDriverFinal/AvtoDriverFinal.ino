#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define trigPin D1  // Pini za distance sensor
#define echoPin D2

#define motorRight D3  
#define motorLeft D4


#define turnTime 300 // Time to turn in ms.
 
const char* ssid = "G-A5";
const char* password = "goskagoska";

int m_status = 0;
String state = "stopped";


void turn(void)
{
    digitalWrite(motorRight, HIGH);
    digitalWrite(motorLeft, LOW);
    
    delay(turnTime);
}
 
void setup () {
   pinMode(trigPin, OUTPUT);  // Distance sensor setup
   pinMode(echoPin, INPUT);

   pinMode(motorRight, OUTPUT);
   pinMode(motorLeft, OUTPUT);
   digitalWrite(motorRight, LOW);
   digitalWrite(motorLeft, LOW);
  
   digitalWrite (trigPin, LOW);
  
 Serial.begin(115200);
 WiFi.begin(ssid, password);
 int i = 0;
 while (WiFi.status() != WL_CONNECTED && i < 10) {
   Serial.print("Connecting..");
   for (int i = 0; i < 10; i++){
     delay(50);
     digitalWrite(D4, LOW);
     delay(50);
     digitalWrite(D4, HIGH);
   }   
 }
 pinMode(D0, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
 digitalWrite(D0, HIGH);     // Initialize the LED_BUILTIN pin as an output 
 pinMode(D4, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
 //digitalWrite(D4, HIGH);     // Initialize the LED_BUILTIN pin as an output
}
 
void loop() {
  HTTPClient http;  //Declare an object of class HTTPClient
  int left = 0;
  int right = 0;
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    /* http.begin("http://phoebe.tano.si:8080/api/robot/instructions");  //Specify request destination
    int httpCode = http.GET(); //Send the request
    if (httpCode > 0) { //Check the returning code
      String payload = http.getString();   //Get the request response payload
      Serial.println(payload);                     //Print the response payload
    } else {
      Serial.println("Error" + String(httpCode));  
    }
    http.end();   //Close connection */
    // delay(200);
    //HTTPClient http;  //Declare an object of class HTTPClient
    if (m_status == 0) {String state = "running";} // or "stopped" or "rotating"
    else String state = "stopped";
    
    http.begin("http://phoebe.tano.si:8080/api/robot/status?state=" + state + "&timestamp=" + String(millis()));  //Specify request destination
    int httpCode = http.GET(); //Send the request
    if (httpCode > 0) { //Check the returning code
    String motor_status = http.getString();
    Serial.println(motor_status); 
    Serial.println(millis()); 
    String mot_status = motor_status.substring(1, 2);
    int m_status = mot_status.toInt();
    http.end();   //Close connection

    digitalWrite(trigPin, HIGH);  // Read distance from distance sensor
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    float distance = pulseIn(echoPin, HIGH)/58.2; // Distance in cm
    Serial.println(distance);

    
    if (m_status == 1){
      if (distance < 25.0){  // Avtoček je prišel do ovire in se sproži ukaz za obrat, da se ji izogne
             Serial.println("Turning...");
              turn();
              http.begin("http://phoebe.tano.si:8080/api/robot/obstacle");  //Obstacle detected
              int httpCode = http.GET();
              http.end();
           }
       else{
        digitalWrite(motorRight, HIGH);
        digitalWrite(motorLeft, HIGH);
       }
            //if (distance < 20.0){  // Avtoček je prišel do ovire in se sproži ukaz za obrat, da se ji izogne
             // Serial.println("Turning...");
              //turn();
           // }
    }

    else {
      digitalWrite(motorRight, LOW);
        digitalWrite(motorLeft, LOW);
    }
    }
    else {
      Serial.println("Error" + String(httpCode));  
    }




    /* 
    if (httpCode > 0) { //Check the returning code
      String payload = http.getString();   //Get the request response payload
      Serial.println(payload);                     //Print the response payload
    } else {
      Serial.println("Error" + String(httpCode));  
    }
    http.end();   //Close connection */  
     
  } else {
    Serial.println("Not connected"); 
  }
}
