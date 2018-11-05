import msvcrt

import cv2
import sys
import os


def detect(id,name):
	# initialize
	cap = cv2.VideoCapture(0)

	cv2.startWindowThread()

	# Create the haar cascade
	# print(sys.path)
	faceCascade = cv2.CascadeClassifier("attendance/haarcascade_frontalface_default.xml")

	# declare value to determine the time and number of pictures
	n = 1
	time = 1
	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()

		# convert the frame to gray color
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE
		)

		font = cv2.FONT_HERSHEY_DUPLEX

		# check if face not found then put message text
		if(len(faces) == 0):
			cv2.putText(frame, "Please put your face in camera", (50,250), font, 1.0, (255,255,255), 1)
		# if face founded
		else:
			cv2.putText(frame, "Press space to take a picture", (50, 50), font, 1.0, (255, 255, 255), 1)
			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

			if cv2.waitKey(1) & 0xFF == ord('p'):
				# # every time mod 45 is zero then increment value and save the frame to image
				# if time % 45 == 0:
				# save the frame to image file
				newPath = 'attendance/dataset/'+ id + '-' + name
				if not os.path.exists(newPath):
					os.makedirs(newPath)

				ret, frame = cap.read()
				cv2.imwrite(newPath + '/' + str(n) + ".jpg", frame)

				cv2.putText(frame, "Picture saved", (50, 250), font, 1.0, (255, 255, 255), 1)
				break
				# n += 1

				# # draw text to give how many number of picture will be taken
				# cv2.putText(frame, "Taking "+ str(5 - n) + " picture left", (50,50), font, 1.0, (255,255,255), 1)

				# increase the time value
				# time += 1


		#Display the resulting frame
		cv2.imshow('frame', frame)

		#waiting for the 'q' keys
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyWindow('frame')
	cv2.destroyAllWindows()


	return "Success"


# if __name__ == "__main__":
# 	try:
# 		arg = sys.argv[0]
# 		arg2 = sys.argv[1]
# 	except IndexError:
# 		arg = None
# 		arg2 = None

	# detect(arg, arg2)
