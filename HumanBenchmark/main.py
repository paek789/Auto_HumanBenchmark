import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui

# 반응속도&에임봇은 humanbenchmark 에서 진행하였습니다

# template1 = cv2.imread('aim.PNG', 0) # 에임봇
template1 = cv2.imread('green.png', 0) # 반응속도

w,h = template1.shape[::-1]


while(1):

        screen = np.array(ImageGrab.grab(bbox=(0, 0, 1200, 800)))

        res1 = cv2.matchTemplate(cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY),  template1, cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc1 = np.where(res1 > threshold)

        print(np.max(res1))
        if np.max(res1) > 0.8:

                # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res1)
                # pyautogui.moveTo(max_loc[0]+15, max_loc[1]+15)
                # pyautogui.click()

                pyautogui.click()
                # 반응속도

        for pt in zip(*loc1[::-1]):
                cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)

        cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break