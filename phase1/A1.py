import cv2

image = input("Enter the image path: ")

img = cv2.imread(image)

if img is not None:
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Do you want to save the image?(y/n)")
    ip= input("Enter the path where you want to save the image: ").lower()
    if ip != "y":
        print("Image not saved")
    else:
        image_path = input("Enter the name of the image(e.g output.png): ")
        cv2.imwrite(image_path, image)
        print("Image saved")
else:
    print("Image not found")