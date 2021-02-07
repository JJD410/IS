from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
import pyautogui
import time 

pyautogui.FAILSAFE = False
TIMELAPSE = 1
acceptButtonImg = "./sample.png"
Count = 0

def checkPointsAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg)
        
        if not pos[0] == -1:
            posx = int(pos[0]) - 1919
            posy = int(pos[1]) 
            pyautogui.click(posx, posy)
            global Count 
            Count += 1
            Total = int(Count * 50)
            print("Total points redeemed by clicking: ", str(Total))
            break
        
        time.sleep(TIMELAPSE)
        
def main():
    run = True

    while run is True:
        checkPointsAvailableLoop()
        time.sleep(TIMELAPSE)


if __name__ == '__main__':
    print("Looking for gold chests...")
    main()