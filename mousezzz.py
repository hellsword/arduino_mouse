import serial, time, pyautogui

arduino = serial.Serial('COM7', 9600)
time.sleep(0.1)
#pyautogui.moveTo( 300+(300+1000)/5 , 300+(300+1000)/5)

print "brutush"
while True:
    x = arduino.readline()
    print("x: "+x)

    x = ""

arduino.close()
