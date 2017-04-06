# Sensor 2: Gyroscope Sensor

Following previous experience, today we will learn go to use gyroscope sensor. We are continuing using the sensor [MPU-6050](https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf), it is a 6-axis MotionTracking device that combines a 3-axis gyroscope, 3-axis accelerometer, and a Digital Motion Processor™ (DMP) all in a small 4x4x0.9mm package.

![6050](pics/mpu-6050.jpg)

 Gyroscopes are used for measuring or maintaining orientation. They can be based on several operating principles such as spinning wheel, the electronic, microchip-packaged MEMS gyroscopes found in consumer electronics devices, solid-state ring lasers, fiber optic gyroscopes, and the extremely sensitive quantum gyroscope.

The gyroscope found in the MPU-6050 sensor is a [MEMS device](http://howtomechatronics.com/how-it-works/electrical-engineering/mems-accelerometer-gyrocope-magnetometer-arduino/). Some MEMS measure the angular rate using the Coriolis Effect others Foucault pendulum concept. When a mass is moving in a particular direction with a particular velocity and when an external angular rate will be applied as show with the green arrow a force will occur, as show with the blue red arrow, which will cause perpendicular displacement of the mass. So similar to the accelerometer, this displacement will cause change in capacitance which will be measured, processed and it will correspond to a particular angular rate.

![Gyroscope](pics/Gyroscope-How-It-Works.png)

A MEMS gyroscope looks like the following diagram. A mass that is constantly moving, or oscillating, and when the external angular rate will be applied a flexible part of the mass would move and make the perpendicular displacement.

![Gyroscopemems](pics/Gyroscope-Microstructure.jpg)

## Soldering and connecting MPU-6050

Please follow the direction given by instructor to solder the pins for your MPU-6050. After finished, connect the sensor using as a reference the following picture:

![diagramsensor](pics/IMG_6779.JPG)

## I2C

The communication between your microcontroller and sensor is by I2C. I2C is an acronym for “Inter-Integrated Circuit”. I2C is a simple and standar data line bus. The data lines travel between various integrated circuits in their products. This reduced the number of wires to two (SDA – data, and SCL – clock). Here is a nice introductory [video](https://www.youtube.com/watch?v=BcWixZcZ6JY) from NXP.

![i2c](pics/I2C-Communication-How-It-Works.png)


## RedBear Code for Gyroscope

The gyroscope can be set at different ranges (°/s is degrees per second): ± 250 °/s, ± 500 °/s, ± 1000 °/s, and ± 2000 °/s. For a ± 250 °/s, you can measure up to 41 RPM ((250°/s/360°) * 60s/min). If you need to measure faster rotations you would have to increase the range, for example, to ± 2000 °/s, which can measure up to 333.3 RPM (but sensitivity is reduced, a trade off!).

For the ranges  ± 250 °/s, ± 500 °/s, ± 1000 °/s, and ± 2000 °/s, the sensitivity is 131 LSB/°/s, 65.5 LSB/°/s, 32.8 LSB/°/s and 16.4 LSB/°/s, respectively.

LSB/unit or Unit/LSB is the factor,called sensitivity, with which you have to multiply the raw sensor data.

* x lsb means - 1 unit
* lsb means - 1/x unit
* value lsb(value in the register) = (1/x) * (value in the register)

For the range ± 500 °/s, we need to divide the raw number by 65.5 LSB/°/s so we can obtain °/s unit.

Using I2C communication, the following [code](https://github.com/jpduarteeecs/hardwaremakers/blob/master/labs_sp17/sensor_accgyro/acc_gyro/acc_gyro.ino) can read data from the MPU-6050:

```Arduino
/* Graph I2C Accelerometer On RedBear Duo over Serial Port
 * This example shows how to program I2C manually
 * I2C Pins SDA1==D0, SCL1 == D1
 * Default address: 0x18
 */

// do not use the cloud functions - assume programming through Arduino IDE
#if defined(ARDUINO)
SYSTEM_MODE(MANUAL);
#endif

#define TXRX_BUF_LEN 20

static uint8_t tx_buf[TXRX_BUF_LEN];

uint8_t tx_value[TXRX_BUF_LEN] = {0,};
uint8_t rx_value[TXRX_BUF_LEN] = {0,};

//Declaring some global variables
int16_t gyro_x, gyro_y, gyro_z;
int16_t acc_x, acc_y, acc_z;
int temperature;
long gyro_x_cal, gyro_y_cal, gyro_z_cal;
long loop_timer;
int lcd_loop_counter;
float angle_pitch, angle_roll;
int angle_pitch_buffer, angle_roll_buffer;
boolean set_gyro_angles;
float angle_roll_acc, angle_pitch_acc;
float angle_pitch_output, angle_roll_output;
float auxx,auxy,auxz;
float auxgx,auxgy,auxgz;
//MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;


void setup() {
  Wire.begin();                                                        //Start I2C as master
  Serial.begin(115200);                                               //Use only for debugging
  pinMode(13, OUTPUT);                                                 //Set output 13 (LED) as output

  setup_mpu_6050_registers();                                          //Setup the registers of the MPU-6050 (500dfs / +/-8g) and start the gyro

  digitalWrite(13, HIGH);                                              //Set digital output 13 high to indicate startup
  digitalWrite(13, LOW);                                               //All done, turn the LED off

  loop_timer = micros();                                               //Reset the loop timer
}

void loop() {
  read_mpu_6050_data();
  //gyro_x -= gyro_x_cal;                                                //Subtract the offset calibration value from the raw gyro_x value
  //gyro_y -= gyro_y_cal;                                                //Subtract the offset calibration value from the raw gyro_y value
  //gyro_z -= gyro_z_cal;                                                //Subtract the offset calibration value from the raw gyro_z value
  auxx=(float)acc_x/4096;
  auxy=(float)acc_y/4096;
  auxz=(float)acc_z/4096;

  auxgx=(float)gyro_x/65.5;
  auxgy=(float)gyro_y/65.5;
  auxgz=(float)gyro_z/65.5;

  Serial.print("a/g:\t");
  Serial.print(auxx); Serial.print("\t");
  Serial.print(auxy); Serial.print("\t");
  Serial.print(auxz); Serial.print("\t");
  Serial.print(auxgx); Serial.print("\t");
  Serial.print(auxgy); Serial.print("\t");
  Serial.println(auxgz);
  delay(100);

}

void read_mpu_6050_data(){                                             //Subroutine for reading the raw gyro and accelerometer data
  Wire.beginTransmission(0x68);                                        //Start communicating with the MPU-6050
  Wire.write(0x3B);                                                    //Send the requested starting register
  Wire.endTransmission();                                              //End the transmission
  Wire.requestFrom(0x68,14);                                           //Request 14 bytes from the MPU-6050
  while(Wire.available() < 14);
  //Wait until all the bytes are received
  acc_x = Wire.read()<<8|Wire.read();                                  //Add the low and high byte to the acc_x variable
  acc_y = Wire.read()<<8|Wire.read();                                  //Add the low and high byte to the acc_y variable
  acc_z = Wire.read()<<8|Wire.read();                                  //Add the low and high byte to the acc_z variable
  temperature = Wire.read()<<8|Wire.read();                            //Add the low and high byte to the temperature variable
  gyro_x = Wire.read()<<8|Wire.read();                                 //Add the low and high byte to the gyro_x variable
  gyro_y = Wire.read()<<8|Wire.read();                                 //Add the low and high byte to the gyro_y variable
  gyro_z = Wire.read()<<8|Wire.read();                                 //Add the low and high byte to the gyro_z variable

}

void setup_mpu_6050_registers(){
  //Activate the MPU-6050
  Wire.beginTransmission(0x68);                                        //Start communicating with the MPU-6050
  Wire.write(0x6B);                                                    //Send the requested starting register
  Wire.write(0x00);                                                    //Set the requested starting register
  Wire.endTransmission();                                              //End the transmission
  //Configure the accelerometer (+/-8g)
  Wire.beginTransmission(0x68);                                        //Start communicating with the MPU-6050
  Wire.write(0x1C);                                                    //Send the requested starting register
  Wire.write(0x10);                                                    //Set the requested starting register
  Wire.endTransmission();                                              //End the transmission
  //Configure the gyro (500dps full scale)
  Wire.beginTransmission(0x68);                                        //Start communicating with the MPU-6050
  Wire.write(0x1B);                                                    //Send the requested starting register
  Wire.write(0x08);                                                    //Set the requested starting register
  Wire.endTransmission();                                              //End the transmission
}

```

## References

* [Arduino Accelerometer & Gyroscope Tutorial MPU-6050 6DOF Module](https://www.youtube.com/watch?v=M9lZ5Qy5S2s)
* [MPU-6050 6dof IMU tutorial for auto-leveling quadcopters with Arduino source code](https://www.youtube.com/watch?v=4BoIE8YQwM8)
* [What is the I2C Bus? An Introduction from NXP](https://www.youtube.com/watch?v=BcWixZcZ6JY)
* [How I2C Communication Works and How To Use It with Arduino](https://www.youtube.com/watch?v=6IAkYpmA1DQ)
