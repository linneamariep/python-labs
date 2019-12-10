import cv2
import math
import cvlib

# Exercise 501
def remove_blue(picture):
    height, width, _ = picture.shape
    for y in range(height):
        for x in range(width):
            picture[y,x][0] = 0

def remove_green(picture):
    height, width, _ = picture.shape
    for y in range(height):
        for x in range(width):
            picture[y,x][1] = 0

def green_sin(picture):
    height, width, _ = picture.shape
    for y in range(height):
        for x in range(width):
            picture[y,x][1] *= ((math.sin(x/20)*math.sin(y/20)+1)/2)



# Exercise 5A1
def cvimg_to_list(picture):
    new_list = []
    height, width, _ = picture.shape
    for y in range(height):
        for x in range(width):
            (b, g, r) = picture[y,x]
            new_list.append((b, g, r))
    return new_list

#Exercise 502
def double_elements(seq):
    return [i*2 for i in seq]


#Exercise 503
def all_pairs_ordered(n):
    return [(x,y) for x in range(n+1) for y in range(n+1)]


#Exercise 504
def distribute(n, seq):
    return [l + [n] for l in seq]


#Uppgfter som Malcolm hittar på
def not_6(n):
    """
    Alla tal från 0 till n som är delbar med 2 MEN inte telet 6.
    """
    return [i for i in range(n+1) if i%2 == 0 and i != 6]


def even_or_odd(n):
    """
    Alla tal 0 till n, om jämt -> "Hej" om udda -> "Okej"
    """
    return ["Hej" if i%2 == 0 else "Okej" for i in range(n+1)]


#Exercise 505



if __name__ == '__main__':
    print(even_or_odd(10))
    #picture = cv2.imread('cat.jpg')
    #green_sin(picture)
    #cv2.imwrite('cat_green_sin.jpg', picture)

    #img = cv2.imread('plane.jpg')
    #list_img = cvimg_to_list(img)
    #converted_img = cvlib.rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])
    #cv2.imshow("converted", converted_img)
    #cv2.waitKey(0)

    #print(all_pairs_ordered(2))

    #print(distribute('k', [['o'], [0, 1, 2], ['o','o']]))

    #print(not_6(10))
