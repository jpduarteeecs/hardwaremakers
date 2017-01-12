//this program read the data from a hc-sr04 sensor and send it to computer using serial comunication
//Juan Duarte, jpduarte@berkeley.edu, Dic 2016
#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

#define trigPin D6 // Trig pin on the HC-SR04
#define echoPin D5 // Echo pin on the HC-SR04

unsigned long distance;
long lastDebounceTime = 0;
long debounceDelay = 50;
boolean activation = true;
char inByte = '0';

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(500);
  digitalWrite(trigPin, LOW);
  distance = pulseIn(echoPin,HIGH);

  if (inByte=='1') {
    if ((distance<300) && activation) {
      lastDebounceTime = millis();
      activation = false;
    }
  
    if ((distance>300) ) {
      activation = true;
    }  
 
    if (((millis() - lastDebounceTime) > debounceDelay) && !activation) {
      // whatever the reading is at, it's been there for longer
      // than the debounce delay, so take it as the actual current state:
  
    Serial.println(distance);
    inByte = '0';
    activation = true;
    }

  } 
    
  if(Serial.available()){ // only send data back if data has been sent
    inByte = Serial.read(); // read the incoming data
  }
  
}






