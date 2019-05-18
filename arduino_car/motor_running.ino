
#define TIME1 20    //čas forward v ms
#define TIME2 15    //čas turn v ms
#define fSpeedD 160 //forward speed desna. To je nekje min., da motorčke poganjaš
#define fSpeedL 250 //forward speed leva

//Definiramo pine
const int enablePin1 = 9;
const int enablePin2 = 10;
const int controlPin1D = 2;
const int controlPin2D = 3;
const int controlPin1L = 6;
const int controlPin2L = 7;

//spremenljivke
int motor1Enabled = 0;
int motor2Enabled = 0;

void forward(void);

void setup() {
   pinMode(enablePin1, OUTPUT);
   pinMode(enablePin2, OUTPUT);
   pinMode(controlPin1D, OUTPUT);
   pinMode(controlPin2D, OUTPUT);
   pinMode(controlPin1L, OUTPUT);
   pinMode(controlPin2L, OUTPUT);
   
   //pinMode(killPin, INPUT);
   
   digitalWrite(controlPin1D, HIGH);
   digitalWrite(controlPin2D, LOW);
   digitalWrite(controlPin1L, HIGH);
   digitalWrite(controlPin2L, LOW);
   digitalWrite(enablePin1, LOW);
   // analogWrite(enablePin2, LOW);
   // analogWrite(enablePin1, LOW);
   // digitalWrite(enablePin2, LOW);
   // digitalWrite(enablePin1, HIGH);
   // digitalWrite(enablePin2, HIGH);

}

void loop() {
  analogWrite(enablePin1, fSpeedD);
  analogWrite(enablePin2, fSpeedL);

}

void forward(void)
{  
    /* analogWrite(enablePin1, fSpeedD);
    analogWrite(enablePin2, fSpeedL);

    delay(TIME1 * 100); */
}
