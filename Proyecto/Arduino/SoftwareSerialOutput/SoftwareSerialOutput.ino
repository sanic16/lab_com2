

#include  <SoftwareSerial.h>

const int rxpin = 2; // pin usado para recivir 
const int txpin = 3; // pin usado para enviar 
SoftwareSerial serial1(rxpin, txpin); // simulando otro puerto UART

void setup() {
  // 9600 baudios tanto para la comunicación con la pc como con el otro arduino
  Serial.begin(9600); 
  serial1.begin(9600);
}

void loop() {
  /*
   * Se juega con las velocidades, es como si fuera simultáneo la 
   * transmisión y recepción para textos pequeños. Para textos muy
   * grandes hay que programar en la computadora que se envie el texto
   * por tiempos regulares, para darle tiempo de responder al receptor.
  */
  if(Serial.available()){
    serial1.print((char)Serial.read());
  }else if(serial1.available()){
    Serial.print((char)serial1.read());
  }
}
