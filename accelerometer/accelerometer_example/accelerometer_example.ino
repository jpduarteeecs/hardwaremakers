/* Graph I2C Accelerometer On RedBear Duo over Serial Port
 * Adafruit Part 2809 LIS3DH - http://adafru.it/2809
 * This example shows how to program I2C manually
 * I2C Pins SDA1==D0, SCL1 == D1
 * Default address: 0x18
 */
 
// do not use the cloud functions - assume programming through Arduino IDE
#if defined(ARDUINO) 
SYSTEM_MODE(MANUAL); 
#endif
// Basic demo for accelerometer readings from Adafruit LIS3DH

#include "Adafruit_LIS3DH.h"
#include "Adafruit_Sensor.h"

#define PI 3.1415
#define button D8

typedef struct ACCEL_DATA {
  float xG, yG, zG;
  float pitch, roll;
};

// Accelerometer 
ACCEL_DATA accel_data;
// I2C
Adafruit_LIS3DH lis = Adafruit_LIS3DH();

void setup(void) {
  
  Serial.begin(9600);
  pinMode(button,INPUT_PULLUP);
  
  LIS3DH_init();
}

void loop() {
  LIS3DH_getData();
  LIS3DH_sendData();
  delay(33); //30Hz update rate
}

boolean LIS3DH_init(void) {
        if(!lis.begin(0x18)) {
                Serial.printf("Couldn't start!\n");
                return 0;
        }
        Serial.printf("LIS3DH Found");

        lis.setRange(LIS3DH_RANGE_4_G);

        Serial.printf("Range = %d G \n",lis.getRange());
        return 1;
}

void LIS3DH_sendData(void) {
        Serial.printf("%f,%f,%i\n",accel_data.pitch,accel_data.roll,!digitalRead(button));
}

void LIS3DH_getData(void) {
        //REMINDER, I2C Pins SDA1==D0, SCL1 == D1
        // get X Y and Z data at once
        lis.read();
        //get a new sensor event, normalized
        sensors_event_t event;
        lis.getEvent(&event);
        //Get the results (acceleration measured in m/s^2)
        accel_data.xG = (event.acceleration.x/(9.8));
        accel_data.yG = (event.acceleration.y/(9.8));
        accel_data.zG = (event.acceleration.z/(9.8));

        accel_data.pitch = atan(accel_data.xG/sqrt(pow(accel_data.yG,2) + pow(accel_data.zG,2)));
        accel_data.roll = atan(accel_data.yG/sqrt(pow(accel_data.xG,2) + pow(accel_data.zG,2)));

        accel_data.pitch = accel_data.pitch * (180/PI);
        accel_data.roll = accel_data.roll * (180/PI);
}


