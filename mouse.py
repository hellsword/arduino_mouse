import serial, time, pyautogui

cuenta_clicks = 0   #Si es distinto a 0, arrastra el elemento, sino hace un click izquierdo

arduino = serial.Serial('COM4', 9600)   #establece la conexion con arduino
time.sleep(0.1)

while True:

    clickIzq = arduino.readline()   #Lee la entrada del boton izquierdo
    clickDer = arduino.readline()   #Lee la entrada del boton derecho

    #lee las coodenadas x e y del acelerometro
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


    #Reviza si se ha hecho click con algun boton
    if cclickIzq == 0:
        cuenta_clicks = 0
    if cclickIzq == 1 and cuenta_clicks == 0:
        cuenta_clicks = cuenta_clicks + 1
        pyautogui.click()
    if cclickDer == 1:
        pyautogui.click(button='right')



    #arriba-derecha
    if xx > 350 and yy > 350:
        if cuenta_clicks != 0:
            pyautogui.dragRel(mov_x_mayor, mov_y_mayor)
        else:
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
        if cuenta_clicks != 0:
            pyautogui.dragRel(0, mov_y_mayor)
        else:
            pyautogui.moveRel(0,mov_y_mayor)
    #abajo
    elif yy < 320:
        pyautogui.moveRel(0,mov_y_menor)
    

    
    clickIzq = ""
    clickDer = ""
    x = ""
    y = ""

arduino.close()
