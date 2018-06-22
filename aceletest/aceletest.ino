/* Programacion de Arduino Uno para utilizar como Mouse en conjunto con Python */

int x, y;

void setup() {
  Serial.begin(9600); // velocidad con nuestro arduino
}

void loop() {

  x = analogRead(A0);
  y = analogRead(A1);
  

/*
  Serial.print(x);//imprimir mensaje del puerto analogico
  Serial.print("   ");
  Serial.println(y);//imprimir mensaje del puerto analogico
  Serial.print("\n ");
*/


  Serial.println(x);
  Serial.println(y);

  delay(100);
  

/*
  if(analogRead(A0) > 500)
  {
    digitalWrite(13,HIGH);
  }else{
    digitalWrite(13,LOW);
  }
  */

}
