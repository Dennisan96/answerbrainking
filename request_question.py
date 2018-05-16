import subprocess
from PIL import Image
from io import StringIO


try:
    import auto_adb
except Exception as ex:
    print(ex)
    exit(1)


adb = auto_adb()


def get_question_from_prompt():
    query = input('Enter the question: ')
    return query

def get_image():
    process = subprocess.Popen(adb.adb_path+' shell screen -p', shell=True, stdout=subprocess.PIPE)
    b_screenshot = process.stdout.read()
    return Image.open(StringIO(b_screenshot))

def get_text():



def get_question_from_screenshot():
    img = get_image()
    query = get_text(img)

    return query


