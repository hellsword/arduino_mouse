# encoding=utf8
import serial
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import serial.tools.list_ports



#Comienza busqueda del puerto donde esta conectado el mouse bluetooth

puerto = ''
#descripcion tecnica
vhwid = str("BTHENUM\{00001101-0000-1000-8000-00805F9B34FB}_LOCALMFG&0045\\7&246DED8&0&301408263330_C00000000")

# Find Live Ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if vhwid in p.hwid:
        puerto = str(p.device)

#Termina busqueda del puerto donde esta conectado el mouse bluetooth

print puerto