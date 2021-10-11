##Imports???

def Read_Voltage(samples,sck,dout):
    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        hx = HX711(dout_pin=dout, pd_sck_pin=sck)

        lastreading = hx._read()
        count = 0
        sum = 0
        while True:
            reading = hx._read()
            if reading == -1:
                lastreading = reading
                pass
            elif count == samples:
                return Voltage_to_Weight(sum/samples)
            elif reading < 0:
                pass
            elif reading == False:
                pass
            elif abs(lastreading/reading) > 1.25 or abs(lastreading/reading) < .75:
                pass
            else:
                sum = sum + reading
            
            count = count + 1
            lastreading = reading    
            time.sleep(.1)
    

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

def Voltage_to_Weight(voltage):
    
    A = 1
    B = 2
    C = 3

    return A*voltage^2 + B*voltage + C

def Calibration():

    import numpy as np

    weight = []
    voltage = []

    for i in range(0, 42, 2):
        i=i/4

        weight.append(i)
        voltage.append(i**5) #Read_Voltage())

    [A,B,C] = np.polyfit(weight, voltage, 2)

    print('A equals:', A)
    print('B equals:', B)
    print('C equals:', C)

if __name__ == "__main__":
    Calibration()


