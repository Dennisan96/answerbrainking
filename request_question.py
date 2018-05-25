import subprocess
from PIL import Image
import pytesseract
from io import StringIO
import auto_adb
from functools import partial

from multiprocessing.dummy import Pool as ThreadPool

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
    # do crop to improve accuracy
    h_width = img.size[0]/2
    h_height = img.size[1]/2
    img_c = img.crop((h_width-500, h_height-400, h_width+500, h_height-80))
    text = pytesseract.image_to_string(img_c, lang='chi_sim')
    return text


def get_choices_from_image(img):
    h_width = img.size[0]/2
    h_height = img.size[1]/2
    img_cl = list()
    #print(pytesseract.image_to_string(img.crop((h_width-300, h_height+80, h_width+300, h_height+210))))
    img_cl.append(img.crop((h_width-300, h_height+80, h_width+300, h_height+210)))
    img_cl.append(img.crop((h_width-280, h_height+273, h_width+280, h_height+400)))
    img_cl.append(img.crop((h_width-300, h_height+470, h_width+300, h_height+590)))
    img_cl.append(img.crop((h_width-300, h_height+660, h_width+300, h_height+800)))
    pool = ThreadPool(4)
    mapfunc = partial(pytesseract.image_to_string, lang='chi_sim')
    cl = pool.map(mapfunc, img_cl)

    print(cl)
    pool.close()
    pool.join()
    return cl


def get_qnc_from_screenshot(debug=False):
    if debug:
        query = input("Enter question: ")
        c = list()
        while True:
            tmp = input("Enter possible choice: ")
            if len(tmp) == 0:
                return query, c
            else:
                c.append(tmp)
    img = get_image()
    h_width = img.size[0] / 2
    h_height = img.size[1] / 2
    img_cl = []
    img_cl.append(img.crop((h_width - 500, h_height - 400, h_width + 500, h_height - 80)))
    img_cl.append(img.crop((h_width-300, h_height+80, h_width+300, h_height+210)))
    img_cl.append(img.crop((h_width-280, h_height+273, h_width+280, h_height+400)))
    img_cl.append(img.crop((h_width-300, h_height+470, h_width+300, h_height+590)))
    img_cl.append(img.crop((h_width-300, h_height+660, h_width+300, h_height+800)))
    pool = ThreadPool(8)
    mapfunc = partial(pytesseract.image_to_string, lang='chi_sim')
    cl = pool.map(mapfunc, img_cl)

    query = cl[0]
    cl.pop(0)
    choice = cl
    print(query)
    print(choice)


    #query = get_question_from_image(img)

    #choice = get_choices_from_image(img)

    return query, choice
