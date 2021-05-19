# import the opencv library
from model import *

# define a video capture object
vid = cv2.VideoCapture(0)
model.eval()
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    transformer = transforms.Compose([
        transforms.ToTensor(),
    ])
    image = [transformer(frame)]
    preds = model(image)
    # Display the resulting frame and boxes
    gain_box_score(frame, preds)
    #cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()