import openrgb , time , string , colorsys
from openrgb.utils import RGBColor , ModeData

client = openrgb.OpenRGBClient()

Dlist = client.devices

def CustomRainbow(speed=1,MaxOffset=30): #Higher = slower
    for Device in Dlist:
        time.sleep(0.3)
        try:
            Device.set_mode('static')
        except:
            Device.set_mode('direct')
        finally:
            pass
            
    Offset = 1
    def P1(CycleSpeed=15):#you must be able to devide 255 by CycleSpeed or THIS WILL NOT WORK
        CBase = []
        R = G = B = 0
        while 1 == 1:
            R += CycleSpeed
            CBase = CBase + [(R,G,B)]
            if R == 255:
                while 1 == 1:
                    G += CycleSpeed
                    CBase = CBase + [(R,G,B)]
                    if G == 255:
                        while 1 == 1:
                            R -= CycleSpeed
                            CBase = CBase + [(R,G,B)]
                            if R == 0:
                                while 1 == 1:
                                    B += CycleSpeed
                                    CBase = CBase + [(R,G,B)]
                                    if B == 255:
                                        while 1 == 1:
                                            G -= CycleSpeed
                                            CBase = CBase + [(R,G,B)]
                                            if G == 0:
                                                while 1 == 1:
                                                    R += CycleSpeed
                                                    CBase = CBase + [(R,G,B)]
                                                    if R == 255:
                                                        while 1 == 1:
                                                            B -= CycleSpeed
                                                            CBase = CBase + [(R,G,B)]
                                                            #print(CBase)
                                                            if B == 0:
                                                                return CBase
    CB = P1()

    CBase = CB

    def wait():
        time.sleep(float('0.000%d'%speed))
    
    Zones = []
    num = 0

    for device in Dlist:
        for zone in device.zones:
            Zones = Zones + [[zone]]
            Offset = 1
            for led in zone.leds:
                Zones[num] = Zones[num] + [[[led],[Offset]]]
                Offset += 1
            num += 1
    
    while True:
        wait()
        for Z in Zones:
            #CheckVal = len(Z) -1
            for LED in Z[1:-1]:
                Color = len(CBase)/MaxOffset
                LEDColor = (int(Color)*LED[1][0])
                if LEDColor >= len(CBase):
                    LEDColor = len(CBase) -1
                CR , CB , CG = CBase[LEDColor]
                LED[0][0].set_color(RGBColor(CR , CB , CG))
                if LED[1][0] >= MaxOffset:
                    LED[1][0] = 1
                else:
                    LED[1][0] += 1

CustomRainbow()