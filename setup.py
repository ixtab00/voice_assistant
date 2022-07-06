import os

def install_win_sound_manager():
    os.system('git clone https://github.com/Paradoxis/Windows-Sound-Manager.git')
    f = open(os.path.join(os.curdir, 'Windows-Sound-Manager', '__init__.py'), 'w')
    f.close()
    f = open(os.path.join(os.curdir, 'Windows-Sound-Manager', 'keyboard.py'), 'r')
    f1 = open(os.path.join(os.curdir, 'Windows-Sound-Manager', 'sound.py'), 'r')
    code = f1.read()[30:]
    f1.close()
    f1 = open(os.path.join(os.curdir, 'Windows-Sound-Manager', 'sound.py'), 'w')
    f1.write(f.read())
    f1.write(code)
    f.close()
    f1.close()
    os.remove(os.path.join(os.curdir, 'Windows-Sound-Manager', 'keyboard.py'))
    os.rename(os.path.join(os.curdir, 'Windows-Sound-Manager'), 'win_sound_mgr')

def main():
    install_win_sound_manager()

if __name__ == '__main__':
    main()