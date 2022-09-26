/*
 * SoftwareSerialOutput sketch
 * Output data to a software serial port
 */

#include  <SoftwareSerial.h>

const int rxpin = 2; // pin used to receive (amarillo)
const int txpin = 3; // pin used to send (blanco)
SoftwareSerial serial1(rxpin, txpin); // new serial port on pins 2 and 3

void setup() {
  Serial.begin(9600); // 9600 baud for the built-in serial port
  serial1.begin(9600);
}

void loop() {
  if(Serial.available()){
    serial1.print((char)Serial.read());
  }else if(serial1.available()){
    Serial.print((char)serial1.read());
  }
}
