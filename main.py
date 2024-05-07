import os
import random
from PIL import Image
from PIL import ImageFont,ImageDraw
import string
from rotate_img import draw_rotated_text
import math
import time

ij = 0
if 'output' in os.listdir(os.getcwd()):  #### create a directory to save the output
     pass
else:   
    os.mkdir('output') 

def random_char(y:int) -> None:
       '''
       This function generates a random characters with the combination of letters numbers and symbols
       '''
       characters =  string.digits
       return ''.join(random.choice(characters) for x in range(y))



def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent
    #print(text_width, text_height)

    return (text_width, text_height)

def create_data(img,x1,x2, y1,y2, imgno)-> None:
    '''
    Function that generate data within any location of custom image
    *Parameters*
    - Image: Path of a blank image
    - X1,X2: Starting point of coordinates horizontal
    - Y1,Y2: Starting point of coordinates vertical 
    - imgno: Number of Image
    '''
    for y in range(0,imgno):
        orig_dir = os.getcwd()
        st = time.time()
        image= Image.open(img) 
        filename, extension = img.split('.')
        font_path = random.choice([
                                   ImageFont.truetype('fonts/inkjet/inkjet-regular.ttf',random.randint(120,130))
                                  ])  #### to choose a font randomly
        
        # ImageFont.truetype('fonts/inkjet/MerchantCopy-GOXq.ttf',random.randint(55,60)),
        # ImageFont.truetype('fonts/inkjet/inkjet-regular.ttf',random.randint(55,60))
        
        line1= "Rs." + random_char(random.randint(2,3)) + " (Re " + "0." + random_char(random.randint(2,3)) + "/ml)  " + chr(random.randint(ord('A'), ord('Z'))) + chr(random.randint(ord('A'), ord('Z'))) + random_char(random.randint(4,7)) + chr(random.randint(ord('A'), ord('Z'))) + '/' + random_char(random.randint(1,2)) 
        line2= chr(random.randint(ord('A'), ord('Z'))) + chr(random.randint(ord('A'), ord('Z'))) + chr(random.randint(ord('A'), ord('Z')))  + " " + random_char(random.randint(4,5)) 
        line3 = chr(random.randint(ord('A'), ord('Z'))) + chr(random.randint(ord('A'), ord('Z'))) + chr(random.randint(ord('A'), ord('Z'))) + " " + random_char(random.randint(4,5))
        # line3 = "MRPRS " + random_char(random.randint(10,12))
        xcor1=random.randint(x1,x2)
        ycor1=random.randint(y1,y2)
        xcor2 = xcor1
        ycor2 = ycor1 + random.randint(110,120)
        xcor3 = xcor1 + random.randint(550,600)
        ycor3 = ycor2 
        rot_ang = random.randint(-1,1)
        #print("time0: ", time.time()-st)
        image = draw_rotated_text(image,rot_ang,(xcor1,ycor1),line1,(0,10,0),font = font_path)
        image = draw_rotated_text(image,rot_ang,(xcor2,ycor2),line2,(0,10,0),font = font_path)
        image = draw_rotated_text(image,rot_ang,(xcor3,ycor3),line3,(0,10,0),font = font_path)
       
        name_image_text = str(time.time())
        op_img_name = os.path.join('output',str(name_image_text) + '.jpg')
        op_txt_name = os.path.join('output',str(name_image_text) + '.txt')

        image.save(op_img_name.format(y))
        #print("time1: ", time.time()-st)
       
        #img1 = ImageDraw.Draw(image)
        
        width1,height1 = get_text_dimensions(line1,font=font_path)
        
     
    ##### For First Rectangle Bounding box
        # calculate the corner points of the unrotated rectangle
        angle1 = -rot_ang
        # print("First Box",angle1)
        top_left1 = (xcor1, ycor1-3)
        top_right1 = (xcor1 + width1+15, ycor1-3)
        bottom_left1 = (xcor1, ycor1 + height1+3)
        bottom_right1 = (xcor1 + width1+15, ycor1 + height1+3)
        # convert the rotation angle to radians
        angle_rad1 = math.radians(angle1)

        # calculate the sin and cosine of the angle
        sin_angle1 = math.sin(angle_rad1)
        cos_angle1 = math.cos(angle_rad1)

        # rotate the corner points around the center point

        if angle_rad1 < 0:
            rotated_top_left1 = (
                xcor1 +  cos_angle1 - (top_left1[1] - ycor1-100) * sin_angle1,
                ycor1 + sin_angle1 + (top_left1[1] - ycor1) * cos_angle1
            )
            rotated_top_right1 = (
                xcor1 + (top_right1[0] - xcor1) * cos_angle1 - (top_right1[1] - ycor1) * sin_angle1,
                ycor1 + (top_right1[0] - xcor1) * sin_angle1 + (top_right1[1] - ycor1) * cos_angle1
            )
            rotated_bottom_left1 = (
                xcor1 + cos_angle1 - (bottom_left1[1] - ycor1-100) * sin_angle1,
                ycor1 + sin_angle1 + (bottom_left1[1] - ycor1) * cos_angle1
            )
            rotated_bottom_right1 = (
                xcor1 + (bottom_right1[0] - xcor1) * cos_angle1 - (bottom_right1[1] - ycor1) * sin_angle1,
                ycor1 + (bottom_right1[0] - xcor1) * sin_angle1 + (bottom_right1[1] - ycor1) * cos_angle1
            )
        else:
            rotated_top_left1 = (
                xcor1 +  cos_angle1 - (top_left1[1] - ycor1+100) * sin_angle1,
                ycor1 + sin_angle1 + (top_left1[1] - ycor1) * cos_angle1
            )
            rotated_top_right1 = (
                xcor1 + (top_right1[0] - xcor1) * cos_angle1 - (top_right1[1] - ycor1) * sin_angle1,
                ycor1 + (top_right1[0] - xcor1) * sin_angle1 + (top_right1[1] - ycor1) * cos_angle1
            )
            rotated_bottom_left1 = (
                xcor1 + cos_angle1 - (bottom_left1[1] - ycor1+100) * sin_angle1,
                ycor1 + sin_angle1 + (bottom_left1[1] - ycor1) * cos_angle1
            )
            rotated_bottom_right1 = (
                xcor1 + (bottom_right1[0] - xcor1) * cos_angle1 - (bottom_right1[1] - ycor1) * sin_angle1,
                ycor1 + (bottom_right1[0] - xcor1) * sin_angle1 + (bottom_right1[1] - ycor1) * cos_angle1
            )

    ######## For Second Rectangle
        width2,height2 = get_text_dimensions(line2,font = font_path)

    ####### calculate the corner points of the unrotated rectangle
        top_left2 = (xcor2 , ycor2-3)
        top_right2 = (xcor2 + width2+15, ycor2-3)
        bottom_left2 = (xcor2, ycor2 + height2+3)
        bottom_right2 = (xcor2 + width2+15, ycor2 + height2+3)

        angle2 = -rot_ang
     
         # convert the rotation angle to radians
        angle_rad2 = math.radians(angle2)

        # calculate the sin and cosine of the angle
        sin_angle2 = math.sin(angle_rad2)
        cos_angle2 = math.cos(angle_rad2)
        
        if angle_rad2 < 0:
            rotated_top_left2 = (
                xcor2 + (top_left2[0] - xcor2) * cos_angle2 - (top_left2[1] - ycor2-100) * sin_angle2,
                ycor2 + (top_left2[0] - xcor2) * sin_angle2 + (top_left2[1] - ycor2) * cos_angle2
            )
            rotated_top_right2 = (
                xcor2 + (top_right2[0] - xcor2) * cos_angle2 - (top_right2[1] - ycor2) * sin_angle2,
                ycor2 + (top_right2[0] - xcor2) * sin_angle2 + (top_right2[1] - ycor2) * cos_angle2
            )
            rotated_bottom_left2 = (
                xcor2 + (bottom_left2[0] - xcor2) * cos_angle2 - (bottom_left2[1] - ycor2-100) * sin_angle2,
                ycor2 + (bottom_left2[0] - xcor2) * sin_angle2 + (bottom_left2[1] - ycor2) * cos_angle2
            )
            rotated_bottom_right2 = (
                xcor2 + (bottom_right2[0] - xcor2) * cos_angle2 - (bottom_right2[1] - ycor2) * sin_angle2,
                ycor2 + (bottom_right2[0] - xcor2) * sin_angle2 + (bottom_right2[1] - ycor2) * cos_angle2
            )

        else:
            rotated_top_left2 = (
                xcor2 + (top_left2[0] - xcor2) * cos_angle2 - (top_left2[1] - ycor2+100) * sin_angle2,
                ycor2 + (top_left2[0] - xcor2) * sin_angle2 + (top_left2[1] - ycor2) * cos_angle2
            )
            rotated_top_right2 = (
                xcor2 + (top_right2[0] - xcor2) * cos_angle2 - (top_right2[1] - ycor2) * sin_angle2,
                ycor2 + (top_right2[0] - xcor2) * sin_angle2 + (top_right2[1] - ycor2) * cos_angle2
            )
            rotated_bottom_left2 = (
                xcor2 + (bottom_left2[0] - xcor2) * cos_angle2 - (bottom_left2[1] - ycor2+100) * sin_angle2,
                ycor2 + (bottom_left2[0] - xcor2) * sin_angle2 + (bottom_left2[1] - ycor2) * cos_angle2
            )
            rotated_bottom_right2 = (
                xcor2 + (bottom_right2[0] - xcor2) * cos_angle2 - (bottom_right2[1] - ycor2) * sin_angle2,
                ycor2 + (bottom_right2[0] - xcor2) * sin_angle2 + (bottom_right2[1] - ycor2) * cos_angle2
            )
        

        
    ######## For Third Rectangle
        width3,height3 = get_text_dimensions(line3,font = font_path)

    ####### calculate the corner points of the unrotated rectangle
        top_left3 = (xcor3 , ycor3-3)
        top_right3 = (xcor3 + width3+15, ycor3-3)
        bottom_left3 = (xcor3, ycor3 + height3+3)
        bottom_right3 = (xcor3 + width3+15, ycor3 + height3+3)

        angle3 = -rot_ang
     
         # convert the rotation angle to radians
        angle_rad3 = math.radians(angle3)

        # calculate the sin and cosine of the angle
        sin_angle3 = math.sin(angle_rad3)
        cos_angle3 = math.cos(angle_rad3)
        
        if angle_rad3 < 0:
            rotated_top_left3 = (
                xcor3 + (top_left3[0] - xcor3) * cos_angle3 - (top_left3[1] - ycor3-100) * sin_angle3,
                ycor3 + (top_left3[0] - xcor3) * sin_angle3 + (top_left3[1] - ycor3) * cos_angle3
            )
            rotated_top_right3 = (
                xcor3 + (top_right3[0] - xcor3) * cos_angle3 - (top_right3[1] - ycor3) * sin_angle3,
                ycor3 + (top_right3[0] - xcor3) * sin_angle3 + (top_right3[1] - ycor3) * cos_angle3
            )
            rotated_bottom_left3 = (
                xcor3 + (bottom_left3[0] - xcor3) * cos_angle3 - (bottom_left3[1] - ycor3-100) * sin_angle3,
                ycor3 + (bottom_left3[0] - xcor3) * sin_angle3 + (bottom_left3[1] - ycor3) * cos_angle3
            )
            rotated_bottom_right3 = (
                xcor3 + (bottom_right3[0] - xcor3) * cos_angle3 - (bottom_right3[1] - ycor3) * sin_angle3,
                ycor3 + (bottom_right3[0] - xcor3) * sin_angle3 + (bottom_right3[1] - ycor3) * cos_angle3
            )

        else:
            rotated_top_left3 = (
                xcor3 + (top_left3[0] - xcor3) * cos_angle3 - (top_left3[1] - ycor3+100) * sin_angle3,
                ycor3 + (top_left3[0] - xcor3) * sin_angle3 + (top_left3[1] - ycor3) * cos_angle3
            )
            rotated_top_right3 = (
                xcor3 + (top_right3[0] - xcor3) * cos_angle3 - (top_right3[1] - ycor3) * sin_angle3,
                ycor3 + (top_right3[0] - xcor3) * sin_angle3 + (top_right3[1] - ycor3) * cos_angle3
            )
            rotated_bottom_left3 = (
                xcor3 + (bottom_left3[0] - xcor3) * cos_angle3 - (bottom_left3[1] - ycor3-100) * sin_angle3,
                ycor3 + (bottom_left3[0] - xcor3) * sin_angle3 + (bottom_left3[1] - ycor3) * cos_angle3
            )
            rotated_bottom_right3 = (
                xcor3 + (bottom_right3[0] - xcor3) * cos_angle3 - (bottom_right3[1] - ycor3) * sin_angle3,
                ycor3 + (bottom_right3[0] - xcor3) * sin_angle3 + (bottom_right3[1] - ycor3) * cos_angle3
            )
        
        ##### To create a annotation files
        ##### For First line
        final_coord1 = []
        final_coord1.append(rotated_top_left1)
        final_coord1.append(rotated_top_right1)
        final_coord1.append(rotated_bottom_right1)
        final_coord1.append(rotated_bottom_left1)
        rect_box1 = []
        for i in final_coord1:
            for j in i:
                rect_box1.append(int(j))

        final_result1 = str(rect_box1).replace('[','').replace(']','') + ', ' + line1
        
        #### For Second line
        final_coord2 = []
        final_coord2.append(rotated_top_left2)
        final_coord2.append(rotated_top_right2)
        final_coord2.append(rotated_bottom_right2)
        final_coord2.append(rotated_bottom_left2)
        rect_box2 = []
        for  k in final_coord2:
            for l in k:
                rect_box2.append(int(l))
        final_result2 = str(rect_box2).replace('[','').replace(']','') + ', ' + line2
        

        ###### For third line

        final_coord3 = []
        final_coord3.append(rotated_top_left3)
        final_coord3.append(rotated_top_right3)
        final_coord3.append(rotated_bottom_right3)
        final_coord3.append(rotated_bottom_left3)
        rect_box3 = []
        for  k in final_coord3:
            for l in k:
                rect_box3.append(int(l))
        final_result3 = str(rect_box3).replace('[','').replace(']','') + ', ' + line3
        


        ##### to display the image
        # image.show()
        # ij = 0
        with open(op_txt_name,'a') as f:
            f.writelines(final_result1)
            f.write('\n')
            f.writelines(final_result2)
            f.write('\n')
            f.writelines(final_result3)
        #     if ij % 20 == 0:
        #         print(ij)
        # ij = ij + 1
        print("Time Taken: ", time.time()-st)
        os.chdir(orig_dir)
        
create_data('real_frooti.jpg',250,250,250,270,70) 
