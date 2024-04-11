## boyaf3 hand detection year 15/5/2021  note : there is a lot of errors i should fix it later ///  DONE EVERTHING OK NO ERROR 
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time
x,y=pyautogui.size()
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(1)
#diffrence=[]

x_postion=""
y_postion=""
prev_frame_time = 0
new_frame_time = 0
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

   
    image.flags.writeable = True
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    h,w,c= image.shape
    def findposition():
     lmlist=[]
     if results.multi_hand_landmarks :
        myhand=results.multi_hand_landmarks[0]
        for id,lm in enumerate(myhand.landmark):
            h,w,c= image.shape
            cx ,cy = int(lm.x* w ), int(lm.y* h) 
            if id == 8:
             lmlist.append([id,cx,cy])
            #if id == 4:
              #lmlist.append([id,cx,cy])
        return lmlist;
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = str(fps)

    #if findposition() != None:
     #a=np.array(findposition())
     #b= np.mean(a)
     #print(b)
    pyautogui.FAILSAFE=False
    if findposition() != None:
     x_postion=findposition()[0][1] * 1280 /1920 *4
     y_postion=findposition()[0][2] * 600 / 1080 *4
     #x = np.interp(x_postion, [0, h], [0, x])
     #y = np.interp(y_postion, [0, w], [0, y])
     print(x_postion)
     print(y_postion)
     pyautogui.moveTo(x=x_postion,y=y_postion)
     currentMouseX, currentMouseY = pyautogui.position()
     print(currentMouseX)
     print(currentMouseY)
     #cv2.putText(image, "x:{},y:{}".format(x_postion,y_postion), color=(255, 0, 0),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,org = (50, 50),fontScale = 1)
     #diffrence.append(findposition()[0][2])
     '''if len(diffrence) > 2:
      if diffrence[0] - diffrence[-1] <= 100:
       if diffrence[0] - diffrence[-1] > 30:
        #pyautogui.doubleClick()'''

    # if b >= 200 :
     # pyautogui.click()
    print(findposition())
  
    #cv2.putText(cv2.flip(image, 1), fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
    print("fps:"+fps)
    cv2.imshow('boyaf3', cv2.flip(image, 1))
    
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()