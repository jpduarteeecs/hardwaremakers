#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

int LED = D7;                         // LED is connected to D7
int analog_read = A1;
int analog_value;

void setup() {
  Serial.begin (9600);
  pinMode(LED, OUTPUT);               // sets pin as output
  pinMode(analog_read, INPUT);  
}

void loop()
{
 analog_value = analogRead(analog_read);
 Serial.println(analog_value);
 delay(100);
}
