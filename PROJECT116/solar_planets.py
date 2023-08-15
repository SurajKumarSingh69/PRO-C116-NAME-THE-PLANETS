import cv2

img=cv2.imread("solar_system.jpg")

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Mercury",
            (20,200),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Venus",
            (40,200),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Earth",
            (60,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Mars",
            (80,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Jupiter",
            (100,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Saturn",
            (120,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Uranus",
            (140,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Neptune",
            (160,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.putText(img,
            "Sun",
            (180,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255
             ))

cv2.imwrite("Solar_systemwithname.jpg ",img)

