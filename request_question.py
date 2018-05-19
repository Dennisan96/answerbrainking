import subprocess
from PIL import Image
import pytesseract
from io import StringIO
import auto_adb


try:
    import auto_adb
except Exception as ex:
    print(ex)
    exit(1)


adb = auto_adb.auto_adb()

def get_question_from_prompt():
    query = input('Enter the question: ')
    return query

def get_image():
    adb.run('shell screencap -p /sdcard/shot1.png')
    adb.run('pull /sdcard/shot1.png')
    return Image.open('./shot1.png')

def get_question_from_image(img):
    #do crop to improve accuracy
    h_width = img.size[0]/2
    h_height = img.size[1]/2
    img_c = img.crop((h_width-500, h_height-400, h_width+500, h_height-80))
    text = pytesseract.image_to_string(img_c, lang='chi_sim')
    return text

def get_choices_from_image(img):
    cl = list()
    h_width = img.size[0]/2
    h_height = img.size[1]/2
    img_c1 = img.crop((h_width-300, h_height+80, h_width+300, h_height+210))
    img_c2 = img.crop((h_width-280, h_height+273, h_width+280, h_height+400))
    img_c2.save('prob.png')
    img_c3 = img.crop((h_width-300, h_height+470, h_width+300, h_height+590))
    img_c4 = img.crop((h_width-300, h_height+660, h_width+300, h_height+800))
    cl.append(pytesseract.image_to_string(img_c1,  lang='chi_sim'))
    cl.append(pytesseract.image_to_string(img_c2,  lang='chi_sim'))
    cl.append(pytesseract.image_to_string(img_c3,  lang='chi_sim'))
    cl.append(pytesseract.image_to_string(img_c4,  lang='chi_sim'))
    print(cl)

    return cl

def get_qnc_from_screenshot():
    img = get_image()
    query = get_question_from_image(img)
    #choice = get_choicse_from_image(img)

    return query


img = get_image()
get_choices_from_image(img)