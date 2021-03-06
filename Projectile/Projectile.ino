#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
 
const char* ssid = "G-A5";
const char* password = "goskagoska";
int drop = 0;
  
void setup () {
 Serial.begin(115200);

 pinMode(D0, OUTPUT);
 pinMode(D6, OUTPUT);
 pinMode(D1, OUTPUT);
 pinMode(D3, OUTPUT);
 
 WiFi.begin(ssid, password);
 while (WiFi.status() != WL_CONNECTED) {
   for (int i = 0; i < 10; i++){
     delay(50);
     digitalWrite(D1, LOW);
     digitalWrite(D3, LOW);
     delay(50);
     digitalWrite(D1, HIGH);
     digitalWrite(D3, HIGH); 
   }
   Serial.print("Connecting..");  
 }

}

void ef(){
    for (int i = 0; i < 10; i++){
     delay(50);
     digitalWrite(D1, LOW);
     digitalWrite(D3, LOW);
     delay(50);
     digitalWrite(D1, HIGH);
     digitalWrite(D3, HIGH); 
   }
}
 
void loop() {
  if (drop == 0){
     digitalWrite(D1, HIGH);
     digitalWrite(D3, HIGH);
     delay(100);
  } else {
     digitalWrite(D1, LOW);
     digitalWrite(D3, LOW);
     delay(500);
     digitalWrite(D1, HIGH);
     digitalWrite(D3, HIGH);
     delay(500);      
  }
  
  HTTPClient http;  //Declare an object of class HTTPClient
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    http.begin("http://phoebe.tano.si:8080/api/robot/drop/get");  //Specify request destination
    int httpCode = http.GET(); //Send the request
    if (httpCode > 0) { //Check the returning code
      String payload = http.getString();   //Get the request response payload
      Serial.println("payload" + payload);                     //Print the response payload
      String leftS = payload.substring(12, 13);
      drop = leftS.toInt();
      Serial.println(drop);                     //Print the response payload
    } else {
      Serial.println("Error" + String(httpCode));  
      ef();
    }
    http.end();   //Close connection   
    
  } else {
    Serial.println("Not connected");
    ef();
  }
}
