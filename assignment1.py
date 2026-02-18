import cv2

photo=input("Enter the file name that you want to load: ")
img=cv2.imread(photo)
if img is not None:
    print("Image loaded succesfully")
    while(1):
        choice=int(input("Press 1 to see the loaded image\nPress 2 to convert the image into grayscale\nPress 0 to exit\nEnter your choice:  "))
        if choice==1:
            cv2.imshow("PHOTO",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice==2:
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            print("Image succesfully converted to gray scale")
            save=input("Do you want to save the gray image?  (y/n?):  ")
            if save.upper()=='Y':
                name=input("enter the file name: ")
                name=name+'.jpg'
                success=cv2.imwrite(name,gray)
                if success:
                    see=input("Gray image successfully saved\nDo you want to see the image?  (y/n?):  ")
                    if see.lower()=='y':
                        cv2.imshow("GRAY PHOTO",gray)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                else:
                    print("Can't save image")
            else:
                see=input("that's fine\nDo you want to see the image?(y/n?):  ")
                if see.lower()=='y':
                        cv2.imshow("GRAY PHOTO",gray)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                else:
                    print("ok! Thanks")
        elif choice==0:
            print("thanks")
            break
else:
    print("Image can't be loaded provide a valid filename!!")