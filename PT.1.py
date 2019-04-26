import numpy as np
import grab_screen, os, pyautogui, cv2, time, io
from PIL import ImageGrab, Image
import pygetwindow as gw
import matplotlib.pyplot as plt

archertower = 'training.PNG'
armytrain = 'armytrain.PNG'
goldstorage = 'Goldstroage.PNG'

#this is for testing and finding where the pointer is on screen
def get_position():
    for i in range(4):
        print(4-i)
        time.sleep(1)
    print(pyautogui.position())

#starts the emulator
def start_em():
    #os.startfile('C:\\Program Files (x86)\\Microvirt\\MEmu\\MEmu.exe')
    #time.sleep(25)
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
    hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,100,100])
    upper_red = np.array([100,190,200])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    resualt = cv2.bitwise_and(original_image, original_image, mask=mask)
    return resualt

#finds the objects
def img_detect(img, imgtofind):
    img_rgb = img
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(imgtofind,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.62
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    return img_rgb


# opens a window showing the edge detection
def screen():
    screen = np.array(ImageGrab.grab(bbox=(0,40,850,520)))
    new_screen = img_detect(screen, archertower)
    new_screen = img_detect(new_screen, armytrain)
    new_screen = img_detect(new_screen, goldstorage)

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
        if os.path.exists('C:\\Program Files (x86)\\Microvirt\\MEmu\\MEmu.exe'):
            start_em()
            em_started = True
        else:
            print('You need to download MEmu')
            print('You can download EMmu at: https://www.memuplay.com/')
            print('or the path is not right should look like')
            print('C:\Program Files (x86)\Microvirt\MEmu\MEmu.exe')
            break
    
    if not clash_started:
        #start_clash()
        clash_started = True
    
    screen()

