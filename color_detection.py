
import cv2
import pandas as pd

img_path = r'C:\Users\nirma\Desktop\pp project\colorpic.jpg'
img = cv2.imread(img_path)

#Declaring Global variables to use in the user defined functions
#Initilasing all the variables with default values
clicked = False
r = g = b = position_x = position_y = 0

# Reading database file with pandas and giving names
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index)
cname=""

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, position_x, position_y, clicked
        clicked = True
        position_x = x
        position_y = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

    cv2.imshow("image", img)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        #Creating String with colour name to display : Color name and RGB values
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)



        clicked = False

    # To exit the menu ESC key is used
    if cv2.waitKey(20) & 0xFF == 27:
        break