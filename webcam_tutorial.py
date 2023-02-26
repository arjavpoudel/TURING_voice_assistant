import cv2 

vid_capture = cv2.VideoCapture(0)

if (vid_capture.isOpened() == False):
  print("error loading file")

else:
  frame_count = vid_capture.get(7)
  print(f"Frame count is: {frame_count}")

  frame_rate = vid_capture.get(5)
  print(f"frame rate is: {frame_rate}")

while (vid_capture.isOpened()):
  ret, frame = vid_capture.read()
  if ret == True:
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(50)
  
    if key == ord('q'):
      break
  else:
    print(f"Cannot output webcam stream since ret value is {ret}")
    break

print(f"ret value: {ret}")

vid_capture.release()

cv2.destroyAllWindows()
