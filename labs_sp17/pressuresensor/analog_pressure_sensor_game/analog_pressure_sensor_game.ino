#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

int LED = D7;                         // LED is connected to D7
int analog_read = A1;
int analog_value;
int state = 0;
char incomingByte = '0'; // for incoming serial data
unsigned long start_time, end_time;

void setup() {
  Serial.begin (9600);
  pinMode(LED, OUTPUT);               // sets pin as output
  pinMode(analog_read, INPUT);  
}

void loop()
{

  switch (state)
  { 
    case 0://waiting for measuring
      state = 0;
      if(Serial.available()){ 
          incomingByte = Serial.read(); // read the incoming data
      
          if (incomingByte=='1') {
            state=1;
            start_time = millis();
          }        
        }      
      break;
    case 1: //calculate time response
      end_time = millis();
      analog_value = analogRead(analog_read);
      if(analog_value>4000){
        Serial.println(end_time-start_time); 
        state = 0;
      } else {
        if(Serial.available()){ 
          incomingByte = Serial.read(); // read the incoming data
        }  
        if (incomingByte=='0') {
          state=0;
        }         
      }
      break;
    default:
      state = 0;
  }

 
}
