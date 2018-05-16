import subprocess
from PIL import Image
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
    adb.run('shell screencap -p /sdcard/shot.png')
    adb.run('pull /sdcard/shot.png')
    return Image.open('./shot.png')

def get_question_from_screenshot():
    img = get_image()
    query = None

    return query


get_image()
