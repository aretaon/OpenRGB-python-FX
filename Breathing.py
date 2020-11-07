import openrgb , time , string , colorsys , sys
from openrgb.utils import RGBColor , ModeData , DeviceType , ZoneType

client = openrgb.OpenRGBClient()

Dlist = client.devices

def SetStatic():
    """A quick function I use to make sure that everything is in direct or static mode"""
    for Device in client.devices:
        time.sleep(0.1)
        try:
            Device.set_mode('direct')
            print('Set %s successfully'%Device.name)
        except:
            try:
                Device.set_mode('static')
                print('error setting %s\nfalling back to static'%Device.name)
            except:
                print("Critical error! couldn't set %s to static or direct"%Device.name)
SetStatic()

def CreateCBase(C = (255,255,255)):
    """Creates a data base of 255 colors to index for use later\n
    So you can grab an RGB color with ``Cbase[num]`` and have a color code\n
    I am not sure if this makes it faster or not but I would assume since it doesn't have to do the math to find out what color it should be
    """
    RunThrough = 0 # determines the amount of passes made
    DevideBase = 0 # the highest value of C (RGB color code)
    BaseC = C #to preserve C for use later (mostly for devision)
    CBase = [] # an empty list to drop the color base into
    for i in C:
        if i > DevideBase:
            DevideBase = i # Redefines DevideBase to be the actually highest instead of 0
    while (C[0] + C[1] + C[2]) > 0: # create a color base for the effect for use later until all three added is == 0 (fade to black)
        AddC = []
        for i in C:
            if (BaseC[C.index(i)] != 0) & (int(BaseC[C.index(i)]) != int(DevideBase)): # the first portion ensure that it isn't trying to devide by 0. the second is to ensure that it doesn't try to devide a number by itself and waste time
                if RunThrough % int(DevideBase / BaseC[C.index(i)]) == 0: # I forgot how this works but it does
                    i -= 1
            else:
                if i > 0: # only subtract if it is greater than 0 (to avoid the SDK yelling at me)
                    i -= 1 # subtract
            AddC = AddC + [i] # add all the numbers together again to get the color code
        RunThrough += 1 # increase the pass amount
        #print(AddC) # print the color code for debugging (will be commented for release)
        C = AddC # This is neccisary for ensure it doesn't get stuck in a loop due to it comparing a static value in the While loop
        CBase = CBase + [C]
    return CBase

def GrabColorOrSpeedOrBoth(Enable=3):
    """Another function for easy copy and pasting\n
    CreateCbase has to be defined for this to work or you have to modify it\n
    You can also enable or disable certain parts (1 is only enable color, 2 is only speed, 3 is both enabled)"""
    if len(sys.argv) > 1:
        if (Enable == 1) or (Enable == 3):
            if (len(sys.argv) == 4):
                CB = CreateCBase(C=(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
                FastGoBRR = 15
                print('user defined color')

        if (Enable == 2) or (Enable == 3):
            if len(sys.argv) == 2:
                CB = CreateCBase()
                FastGoBRR = int(sys.argv[1])
                print('user defined speed')
                if len(CB)%FastGoBRR != 0:
                    print('255 is not devisable by %f (Defaulting to 15)\nPlease try to pick a number that is'%FastGoBRR)
                    FastGoBRR = 15
    
        if (Enable == 3):
            if len(sys.argv) == 5:
                CB = CreateCBase(C=(int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])))
                FastGoBRR = int(sys.argv[1])
                print('user defined both')
    
    else:
        CB = CreateCBase()
        FastGoBRR = 15
        print('nothing is user defined')
    return CB, FastGoBRR

def FBounce(ColorWall,Speed): # makes the lights get brighter
    for color in ColorWall:
        if (ColorWall.index(color)%Speed == 0) or (ColorWall.index(color) == 254):
            if (ColorWall.index(color) == 254):
                for Device in Dlist:
                    Device.set_color(RGBColor(color[0], color[1], color[2]))
                    time.sleep(0.1)
            else:
                for Device in Dlist:
                    Device.set_color(RGBColor(color[0], color[1], color[2]))
                    time.sleep(0.01)
    time.sleep(2)

def BBounce(ColorWall,Speed): # makes the lights get darker
    for color in reversed(ColorWall):
        if (ColorWall.index(color)%Speed == 0):
            for Device in Dlist:
                Device.set_color(RGBColor(color[0], color[1], color[2]))
                time.sleep(0.01)

if __name__ == '__main__':
    LotsOfColors, Speed = GrabColorOrSpeedOrBoth()
    while True:
        FBounce(LotsOfColors,Speed)
        BBounce(LotsOfColors,Speed)
