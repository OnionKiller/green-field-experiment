import cv2
import cvzone
import numpy as np
count = 0
ground_color = None
while True:
    _ ,img = cap.read()
    if ground_color is None:
        ground_color = img[int(img.shape[0]/2) ,int(img.shape[1]/2)]
    img_contours = img.copy()
    dh, dw, _ = img.shape
    count += 1
    # person_file = open(f"../DFL/train_lables/1606b0e6_0_{35000 + count}.txt", 'r')
    # person_file = open(f"labels/08fd33_0_{count}.txt", 'r')
    # person_records = person_file.readlines()
    # person_file.close()

    # for dt in person_records:
    # obj_idx, x, y, w, h = map(float, dt.split(' '))
    # x_c,y_c,l,t,r,b = object_postion_finder(x,y,w,h)
    # cv2.rectangle(img ,(l - 10,t-10) ,(r+10,b+10) ,ground_color.tolist(),-1)

    #converting into hsv image
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #green range
    lower_green = np.array([39,78,153]) # This value is for 1st image
    upper_green = np.array([127, 131, 219]) # This value is for 1st image

    #Define a mask ranging from lower to uppper
    mask = cv2.inRange(hsv, lower_green, upper_green)
    #Do masking
    res = cv2.bitwise_and(img, img, mask=mask)
    #convert to hsv to gray
    res_bgr = cv2.cvtColor(res,cv2.COLOR_HSV2BGR)
    img_blur = cv2.medianBlur(res_bgr ,5)
    img_gray = cv2.cvtColor(img_blur ,cv2.COLOR_BGR2GRAY)

    # threshold1 = cv2.getTrackbarPos("threshold1","Parameters")
    # threshold2 = cv2.getTrackbarPos("threshold2","Parameters")
    v = np.median(img_gray)
    sigma = 0.33
    #---- apply optimal Canny edge detection using the computed median----
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    # print(threshold1,threshold2)

    img_canny = cv2.Canny(img_gray,lower_thresh,upper_thresh)

    img_stack = cvzone.stackImages(([img,img_canny]) ,2,0.2)

    cv2.imshow("Result" ,img_stack)
    key = cv2.waitKey(1)
    if key == 115: # press "S" to break the loop
        break
    cap.release()
    cv2.destroyAllWindows()