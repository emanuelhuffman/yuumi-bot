import pyautogui as auto
import time

time.sleep(2)
win = auto.getActiveWindow()     
#topleft of window
initX = win.topleft.x
initY = win.topleft.y

itemOneX, itemOneY = 623, 703
itemTwoX, itemTwoY = 649, 703
itemThreeX, itemThreeY = 677, 703
itemFour = 1,2
itemFive = 1,2
itemSix = 1,2
ward = 1,2


try:
    while True:
        x, y = auto.position()
        r,g,b = auto.pixel(x, y)

        strRGB = 'x: ' + str(x - initX) + 'y: ' + str(y - initY) + ' r: ' + str(r).rjust(4) + ' g: ' + str(g).rjust(4) + ' b: ' + str(b).rjust(4)

        
        print(strRGB)

        #positionStr = 'X: ' + str(x - addX).rjust(4) + ' Y: ' + str(y - addY).rjust(4) + '---' + str(r) + ',' + str(g) + ',' + str(b)
        #print(positionStr, end='')
        #print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')