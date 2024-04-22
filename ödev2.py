import cv2
import numpy as np

def detect_red_object(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #resmi griye çevirme

    
    lower_red = np.array([0, 100, 100])   #kırmızı sınırları belirleme
    upper_red = np.array([10, 255, 255])

    
    mask = cv2.inRange(hsv, lower_red, upper_red)   #kendi içinde hazır aralık fonk var renk tepiti için
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result

cap = cv2.VideoCapture(0)
//bu bir python projesi
while True:
    ret, frame = cap.read()

    result = detect_red_object(frame)  #burası kırmızıyı tespit ediyor

    # Sonuçları gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Red Object Detection', result)

    # Çıkış için 'q' tuşuna basılmasını kontrol etme
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()