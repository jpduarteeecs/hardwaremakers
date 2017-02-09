//this program read the data from a hc-sr04 sensor and send it to computer using serial comunication
//Juan Duarte, jpduarte@berkeley.edu, Dic 2016
#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

#define trigPin D6 // Trig pin on the HC-SR04
#define echoPin D5 // Echo pin on the HC-SR04

unsigned long distance;
unsigned long distance_sum=0;
unsigned long count=0;
unsigned long sample_number=10;
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
    if (count<sample_number) {
      count+=1;
      distance_sum+=distance;
    } else {
      Serial.println(distance_sum/sample_number);
      inByte = '0';
      count = 1;
      distance_sum=0;
    }

  }

  //#################################data from computer begin#######################
  if(Serial.available()){ // only send data back if data has been sent
    inByte = Serial.read(); // read the incoming data
  }
  //#################################data from computer end#######################

}
