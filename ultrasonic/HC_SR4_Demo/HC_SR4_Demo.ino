//https://www.hackster.io/hypnopompia/internet-controlled-adjustable-height-standing-desk-abd6e8
#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif





/*
HC-SR04 Ping distance sensor]
VCC to arduino 5v GND to arduino GND
Echo to Arduino pin 13 Trig to Arduino pin 12
Red POS to Arduino pin 11
Green POS to Arduino pin 10
560 ohm resistor to both LED NEG and GRD power rail
More info at: http://goo.gl/kJ8Gl
Original code improvements to the Ping sketch sourced from Trollmaker.com
Some code and wiring inspired by http://en.wikiversity.org/wiki/User:Dstaub/robotcar
*/
#define trigPin D6 // Trig pin on the HC-SR04
#define echoPin D5 // Echo pin on the HC-SR04

unsigned long distance;

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(500);
  digitalWrite(trigPin, LOW);
  //Serial.println(state);
  //delayMicroseconds(4500);
  //time1 = micros(); //start or reset timer on every rising edge
  distance = pulseIn(echoPin,HIGH);
  Serial.println(distance);
  delay(100);
  //duration = pulseIn(echoPin, HIGH);  
}






