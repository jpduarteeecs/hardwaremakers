//this program read the data from a hc-sr04 sensor and send it to computer using serial comunication
//Juan Duarte, jpduarte@berkeley.edu, Dic 2016
#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

#define trigPin D6 // Trig pin on the HC-SR04
#define echoPin D5 // Echo pin on the HC-SR04

unsigned long distance;
unsigned long threshold_low = 350;
unsigned long threshold_high = 800;
unsigned long window = 200;

unsigned long distance_previous;

long lastDebounceTime = 0;
long debounceDelay = 50;
boolean activation = true;

char inByte = '1';

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  //#################################sensor begin#####################
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(500);
  digitalWrite(trigPin, LOW);
  distance = pulseIn(echoPin,HIGH);
  //#################################sensor end#######################

  if (inByte=='1') {
    if ((distance<(threshold_low+window)) && activation) {
      lastDebounceTime = millis();
      activation = false;
      distance_previous = threshold_low;
    } 
    if ((distance<(threshold_high+window)) && (distance>(threshold_high-window)) && activation) {
      lastDebounceTime = millis();
      activation = false;
      distance_previous = threshold_high;
    } 
  
    if ((distance>(distance_previous+window)) && (distance<(distance_previous-window)) && !activation) {
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

  //#################################data from computer begin#######################
  if(Serial.available()){ // only send data back if data has been sent
    inByte = Serial.read(); // read the incoming data
  }
  //#################################data from computer end#######################
  
}






