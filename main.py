from Omok.Omok import *
import time

omok = None
a = 30
def main():
    global omok
    omok = Omok(15, a)
    omok.setEvent("<Button-1>", black)
    omok.setEvent("<Button-2>", func)
    omok.setEvent("<Button-3>", white)
    '''print(omok.putStone(0, 5, 1))
    time.sleep(0.5)
    print(omok.putStone(1, 6, 1))
    time.sleep(0.5)
    print(omok.putStone(5, 7, 1))
    time.sleep(0.5)
    print(omok.putStone(6, 8, 1))
    time.sleep(0.5)
    print(omok.putStone(7, 8, 1))
    time.sleep(0.5)
    print(omok.putStone(8, 8, 1))
    time.sleep(0.5)
    print(omok.putStone(5, 8, 1))
    time.sleep(0.5)
    print(omok.putStone(9, 8, 1))
    time.sleep(0.5)
    print(omok.getMap())
    omok.showMap()'''
    
def black(event):
    print(int(event.x / a- 0.5), int(event.y / a- 0.5))
    print(omok.putStone(int(event.x / a- 0.5), int(event.y /a - 0.5), 1))
    
def white(event):
    print(omok.putStone(int(event.x / a- 0.5), int(event.y /a- 0.5), 2))
    
def func(event):
    omok.showMap()

main()