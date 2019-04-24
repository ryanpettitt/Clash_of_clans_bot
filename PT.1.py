import numpy as np
import grab_screen, os, pyautogui, cv2, time, io
from PIL import ImageGrab, Image
import pygetwindow as gw

#this is for testing and finding where the pointer is on screen
def get_position():
    for i in range(4):
        print(4-i)
        time.sleep(1)
    print(pyautogui.position())

#starts the emulator
def start_em():
    os.startfile('C:\\Program Files (x86)\\Microvirt\\MEmu\\MEmu.exe')
    time.sleep(15)
    memu = gw.getWindowsWithTitle('MEmu')[0]
    # Has an add portion with the same name
    if len(gw.getWindowsWithTitle('MEmu')) == 2:
        memu.activate()
        memu.close()
        memu = gw.getWindowsWithTitle('MEmu')[0]
        
    memu.activate()
    memu.resizeTo(850, 520)
    memu.moveTo(0, 0)

# Clicks on the position where clash should be
def start_clash():
    time.sleep(1)
    pyautogui.click(x=136, y=260)


# edge detection
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=400)
    return processed_img

# opens a window showing the edge detection
def screen():
    screen = np.array(ImageGrab.grab(bbox=(0,40,850,520)))
    new_screen = process_img(screen)
    cv2.imshow('window', new_screen)
    #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        run =  False


run = True
attack = False
stop = True
em_started = False
clash_started = False

# main loop
while(run):
    if not em_started:
        if os.path.exists('C:\\Program Files (x86)\\Microvirt\\MEmu'):
            start_em()
            em_started = True
        else:
            print('You need to download MEmu')
            break
    
    if not clash_started:
        start_clash()
        clash_started = True
    
    screen()

