import os
import subprocess
import platform

conf = {
    0: {
        "x": 540,
        "y": 1040,
    },

    1: {
        "x": 540,
        "y": 1230,
    },

    2: {
        "x": 540,
        "y": 1420,
    },

    3: {
        "x": 540,
        "y": 1610,
    }

}

class auto_adb():
    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join('Tools', "adb", 'adb.exe')
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    pass
            print('请安装 ADB 及驱动并配置环境变量')
            print('具体链接: https://github.com/wangshub/wechat_jump_game/wiki')
            exit(1)

    def run(self, raw_command):
        command = '{} {}'.format(self.adb_path, raw_command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        #print(type(process))
        output = process.stdout.read()
        return output


def tap(option):
    os.popen('adb shell input tap {0} {1}'.format(conf[option]['x'], conf[option]['y']))