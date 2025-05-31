import cv2
import os

try:
    dicrectory = r"C:\Users\prati\OneDrive\Desktop\Custon_Object_Detection_GUI\Image_Capturing"
    path = os.path.join(dicrectory, "images")
    os.mkdir(path)
except:
    print("\images directory already exists :D")

new_dicrectory = r"C:\Users\prati\OneDrive\Desktop\Custon_Object_Detection_GUI\Image_Capturing\images"
os.chdir(new_dicrectory)

def main():

    i = 0

    try:
        cam = cv2.VideoCapture(0)

        while True:
            
            ret,img = cam.read()
            cv2.imshow('webcam',img)

            key = cv2.waitKey(1)
            if key == 27:
                break # on ESC key
            elif key == ord('s'):
                print("save")
                image_name = str(i) + ".jpg"
                cv2.imwrite(image_name, img)
                i += 1

        cv2.destroyAllWindows()
        cam.release()
        print("Turning off camera.")
        print("Program end")

    except(KeyboardInterrupt):

        print("Turning off camera.")
        cam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()