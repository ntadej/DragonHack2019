#include <Servo.h>

Servo servo; // Define our Servo
int pos = 0;    // variable to store the servo position
const int servoPin = 9;
int servoDelay=25;

void setup() {
  servo.attach(servoPin);
}

void loop() {
   servo.write(45);      // Turn SG90 servo Left to 45 degrees
   delay(1000);          // Wait 1 second
   servo.write(90);      // Turn SG90 servo back to 90 degrees (center position)
   delay(1000);          // Wait 1 second
   servo.write(135);     // Turn SG90 servo Right to 135 degrees
   delay(1000);          // Wait 1 second
   servo.write(90);      // Turn SG90 servo back to 90 degrees (center position)
   delay(1000);
}
