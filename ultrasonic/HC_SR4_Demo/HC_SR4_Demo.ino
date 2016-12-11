//https://www.hackster.io/hypnopompia/internet-controlled-adjustable-height-standing-desk-abd6e8
#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

#include "Ultrasonic.h"

#define trigPin D6 // Trig pin on the HC-SR04
#define echoPin D5 // Echo pin on the HC-SR04

Ultrasonic ultrasonic(trigPin,echoPin);

void setup() {
Serial.begin(9600);
delay(1000);

}

void loop()
{
  //lcd.clear();
  Serial.printf("Ultrasonic: %d\n",ultrasonic.Ranging(CM));
  delay(100);
}







