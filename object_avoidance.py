import serial
import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BCM)
port = serial.Serial("/dev/serial0", 9600, timeout=0.5)

GPIO_TRIGGER1 = 18
GPIO_ECHO1 = 24
GPIO_TRIGGER2 = 23
GPIO_ECHO2 = 22
GPIO_TRIGGER3 = 17
GPIO_ECHO3 = 27

GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)


def goforward():
    port.write('A')       #go
    rcv = port.read(10)
    print rcv

def turnleft():
    port.write('X')       #left for 1 sec
    rcv = port.read(10)
    print rcv

def turnright():
    port.write('Y')       #right for 1 sec
    rcv = port.read(10)
    print rcv

def stopmotors(): 
    port.write('C')       #stop
    rcv = port.read(10)
    print rcv

def distance2():
        # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER2, False)
    # Allow module to settle
    time.sleep(0.2)
    GPIO.output(GPIO_TRIGGER2, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
   
    TimeElapsed = StopTime - StartTime
    distance2 = (TimeElapsed * 34300) / 2
    print("sensor 2:")
    print ("Measured Distance = %.1f cm" % distance2)
 
    return distance2    
    
def distance1():
        # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER1, False)
    # Allow module to settle
    time.sleep(0.2)
    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()    

    TimeElapsed = StopTime - StartTime
    distance1 = (TimeElapsed * 34300) / 2
    print("sensor 1:")
    print ("Measured Distance = %.1f cm" % distance1)

    return distance1


def distance3():
        # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER3, False)
    # Allow module to settle
    time.sleep(0.2)
    GPIO.output(GPIO_TRIGGER3, True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER3, False)
 
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO3) == 0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO3) == 1:
        StopTime = time.time()
  
    TimeElapsed = StopTime - StartTime
    distance3 = (TimeElapsed * 34300) / 2
    print("sensor 3:")
    print ("Measured Distance = %.1f cm" % distance3)
 
    return distance3


def checkanddrivefront():
    while distance2() < 10:
          stopmotors()
          if distance3 > distance1:
             turnleft()
             goforward()
          if distance1 > distance3:
             turnright()
             goforward()    

def checkanddriveright():
    while distance1() < 10:
        stopmotors()
        turnleft()
    goforward()

def checkanddriveleft():
    while distance3() < 10:
        stopmotors()
        turnright()
    goforward() 

def obstacleavoiddrive():
    goforward()
    while True:
        if distance2() < 10:
            stopmotors()
            checkanddrivefront()
        elif distance1() < 10:
            stopmotors() 
            checkanddriveright()
        elif distance3() < 10:
            stopmotors()
            checkanddriveleft()      

def main():
    print "start driving: "
    # Start obstacle avoid driving
    obstacleavoiddrive()

if __name__ == "__main__":
    main() 
