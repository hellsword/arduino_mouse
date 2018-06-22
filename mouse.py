import serial, time, pyautogui

arduino = serial.Serial('COM8', 9600)
time.sleep(0.1)
#pyautogui.moveTo( 300+(300+1000)/5 , 300+(300+1000)/5)

while True:

    clickIzq = arduino.readline()
    clickDer = arduino.readline()
    x = arduino.readline()
    y = arduino.readline()
    
    print("clickIzq: "+clickIzq)
    print("clickDer: "+clickDer)
    print("x: "+x)
    print("y: "+y)

    cclickIzq = int(clickIzq)
    cclickDer = int(clickDer)
    xx = int(x)
    yy = int(y)
    
    mov_x_mayor = -(350 - xx)
    mov_y_mayor = 350 - yy

    mov_x_menor = -(320 - xx)
    mov_y_menor = 320 - yy


    #Reviza si se ha hecho click
    if cclickIzq == 1:
        pyautogui.click()
    if cclickDer == 1:
        pyautogui.click(button='right')



    #arriba-derecha
    if xx > 350 and yy > 350:
        pyautogui.moveRel(mov_x_mayor,mov_y_mayor)
    #abajo-derecha
    elif xx > 350 and yy < 320:
        pyautogui.moveRel(mov_x_mayor,mov_y_menor)
    #arriba-izquierda
    elif xx < 320 and yy > 350:
        pyautogui.moveRel(mov_x_menor,mov_y_mayor)
    #abajo-izquierda
    elif xx < 320 and yy < 320:
        pyautogui.moveRel(mov_x_menor,mov_y_menor)
    #derecha
    elif xx > 350:
        pyautogui.moveRel(mov_x_mayor,0)
    #izquierda
    elif xx < 320:
        pyautogui.moveRel(mov_x_menor,0)
    #arriba
    elif yy > 350:
        pyautogui.moveRel(0,mov_y_mayor)
    #abajo
    elif yy < 320:
        pyautogui.moveRel(0,mov_y_menor)
    

    
    clickDer = ""
    x = ""
    y = ""

arduino.close()
