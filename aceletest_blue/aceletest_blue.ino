/* Programacion de Arduino Uno para utilizar como Mouse en conjunto con Python, conectado a bluetooth */

#include <SoftwareSerial.h>

int x, y;
int clickIzq, clickDer;

// Constantes para definir los pines
const int rxPin = 3;
const int txPin = 2;
const int leftClick = 4;
const int rightClick = 5;

SoftwareSerial bluetooth(rxPin, txPin);

void setup() {
  // Activamos los pines de entrada y salida
  pinMode(leftClick, INPUT);
  pinMode(rightClick, INPUT);
  
  Serial.begin(9600);
  bluetooth.begin(9600); //set baud rate
}

void loop() {

  clickIzq = digitalRead(leftClick);
  clickDer = digitalRead(rightClick);
  x = analogRead(A0);
  y = analogRead(A1);
  

  bluetooth.println(clickIzq);
  bluetooth.println(clickDer);
  bluetooth.println(x);
  bluetooth.println(y);
  
  delay(100); 

  //delay(1000);
}

