import cv2

image = cv2.imread('phase2/N.png')

# if image is not None:
#     M = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), 45, 1)
#     rotated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#     cv2.imshow('Rotated Image', rotated_image) # display the rotated image
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Image not found")

# if image is not None:
#     h, w, c = image.shape # it will print the shape( height, width , channels) of the image

#     print("height:", h)
#     print("width:", w)
#     print("channels:", c)
#     M = cv2.getRotationMatrix2D((w / 2, h / 2), 35, 1)
#     rotated_image = cv2.warpAffine(image, M, (w, h))
#     cv2.imshow('Rotated Image', rotated_image) # display the rotated image
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Image not found") 

if image is not None:
    # flipped = cv2.flip(image, 1)  # flip the image horizontally
    # flipped = cv2.flip(image, 0)  # flip the image vertically
    flipped = cv2.flip(image, -1)  # flip the image both horizontally and vertically
    cv2.imshow('Flipped Image', flipped) # display the flipped image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image not found")