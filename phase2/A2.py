import cv2

image = input("Enter the image path: ")

img = cv2.imread(image)

def display():
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def basics():
    print("Press 'd' for drawing lines")
    print("Press 'c' for drawing circles")
    print("Press 'r' for drawing rectangles")
    print("Press 't' for adding text")
    aa= input("Enter the operations that you want to perform")
    if aa == 'd':
        x1, y1 = input("Enter the starting point of the line: ").split(',')
        x2 , y2 = input("Enter the ending point of the line: ").split(',')
        image = cv2.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif aa == 'c':
        x, y = input("Enter the center of the circle: ").split(',')
        r = input("Enter the radius of the circle: ")
        image = cv2.circle(image, (int(x), int(y)), int(r), (0, 0, 255), 2)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif aa == 'r':
        x1, y1 = input("Enter the top-left corner of the rectangle: ").split(',')
        x2 , y2 = input("Enter the bottom-right corner of the rectangle: ").split(',')
        image = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif aa == 't':
        text = input("Enter the text: ")
        x, y = input("Enter the position of the text: ").split(',')
        font = cv2.FONT_HERSHEY_SIMPLEX
        image = cv2.putText(image, text, (int(x), int(y)), font, 1, (0, 0, 255), 2)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("Invalid operation")


def extra():
    print("Press 'r' for rotating the image")
    print("Press 'f' for flipping the image")
    print("press 't' for scaling the image")
    print("press 'c' for cropping the image")
    aa= input("Enter the operations that you want to perform")
    if aa == 'r':
        angle = input("Enter the angle of rotation: ")
        image = cv2.rotate(image, angle )
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif aa == 'f':
        print("Press 'h' for flipping the image horizontally")
        print("Press 'v' for flipping the image vertically")
        print("press any key to flip image horizontally and vertically")
        ii = input("Enter the operation that you want to perform: ")
        if ii == 'h':
            image = cv2.flip(image, 1)
            cv2.imshow('Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif ii == 'v':
            image = cv2.flip(image, 0)
            cv2.imshow('Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            image = cv2.flip(image, -1)
            cv2.imshow('Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    elif aa=='t':
        print("Press 's' for scaling the image")
        print("Press 'd' for displaying the image")
        bb = input("Enter the operation that you want to perform: ")
        if bb == 's':
            scale = input("Enter the scale factor: ")
            image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif bb == 'd':
            display()
        else:
            print("Invalid operation")

    elif aa=='c':
        print("Press 's' for cropping the image")
        print("Press 'd' for displaying the image")
        bb = input("Enter the operation that you want to perform: ")
        if bb == 's':
            x1, y1 = input("Enter the starting point of the crop: ").split(',')
            x2 , y2 = input("Enter the ending point of the crop: ").split(',')
            image = image[int(y1):int(y2), int(x1):int(x2)]
            cv2.imshow('Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif bb == 'd':
            display()
        else:
            print("Invalid operation")
        


    if aa == 'r' or aa == 'f' or aa == 't' or aa == 'c':
        print("Press 's' for saving the image")
        print("Press 'd' for displaying the image")
        bb = input("Enter the operation that you want to perform: ")
        if bb == 's':
            image_path = input("Enter the name of the image(e.g output.png): ")
            cv2.imwrite(image_path, image)
            print("Image saved")
        elif bb == 'd':
            display()
        else:
            print("Invalid operation")
    else:
        print("Invalid operation")


if image is not None:
    a= input(print("Press 'f' to perform operation like cropping, scaling, rotating and flipping /n press 'e' for operations like drawing lines drawing circles, drawing rectangles and text"))
    if a == 'f':
        extra()
    elif a == 'e':
        basics()
    else:
        print("Invalid operation")
else:
    print("Image not found")