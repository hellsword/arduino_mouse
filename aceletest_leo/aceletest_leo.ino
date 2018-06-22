/* Programacion de mouse en Arduino leonardo utilizando biblioteca Mouse.h  */

#include <Mouse.h>

int x, y;
int mov_x_mayor, mov_y_mayor;
int mov_x_menor, mov_y_menor;

void setup() {
  Mouse.begin();
  Serial.begin(9600); // velocidad con nuestro arduino
}

void loop() {

  x = analogRead(A0);
  y = analogRead(A1);
  
  mov_x_mayor = -(350 - x);
  mov_y_mayor = 350 - y;

  mov_x_menor = -(320 - x);
  mov_y_menor = 320 - y;



  if(x > 350 and y> 350)
      Mouse.move(mov_x_mayor, mov_y_mayor, 0);
  else if( x > 350 and y < 320)
      Mouse.move(mov_x_mayor, mov_y_menor, 0);
  else if( x < 320 and y > 350)
      Mouse.move(mov_x_menor, mov_y_mayor, 0);
  else if( x < 320 and y < 320)
      Mouse.move(mov_x_menor, mov_y_menor, 0);
  else if( x > 350)
      Mouse.move(mov_x_mayor, 0, 0);
  else if( x < 320)
      Mouse.move(mov_x_menor, 0, 0);
  else if( y > 350)
      Mouse.move(0, mov_y_mayor, 0);
  else if( y < 320)
      Mouse.move(0, mov_y_menor, 0);

  delay(50);
}
