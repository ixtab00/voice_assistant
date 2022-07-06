import sys
import webbrowser
import os
from win_sound_mgr import sound

class Command_evaluator():
    def __init__(self):
        self.comm_to_func = {
            'sub':self._sub_func,
            'search_1':self._search_func_1,
            'search_2':'',
            'search_3':'',
            'task_manager':self._taskmgr,
            'system_settings':self._control,
            'close':self._close,
            'new_tab':self._webbrowser,
            'enable_sound':self._enable_sound,
            'disable_sound':self._disable_sound
        }
        self.curvol = sound.Sound.current_volume()
    
    def evaluate(self, key, features):
        return self.comm_to_func[key](features)
    
    def _sub_func(self, features):
        return str(features[0] - features[1])
    
    def _search_func_1(self, features):
        webbrowser.open('https://www.google.com//search?q=' + '+'.join(features))
        return 'Найдено!\n'
    
    def _webbrowser(self, features):
        webbrowser.open('https://www.google.com/')
        return 'Исполнено!\n'
    
    def _taskmgr(self, features):
        os.system('taskmgr.exe')
        return 'Исполнено!'
    
    def _control(self,features):
        os.system('control')
        return 'Исполнено!'
    
    def _close(self, features):
        sys.exit()
    
    def _disable_sound(self, features):
        self.curvol = sound.Sound.current_volume()
        sound.Sound.mute()
        sound.Sound.volume_set(self.curvol)
        return 'Исполнено!'
    
    def _enable_sound(self, features):
        self.curvol = sound.Sound.current_volume()
        sound.Sound.mute()
        sound.Sound.volume_set(self.curvol)
        return 'Исполнено!'