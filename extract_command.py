import re

class Command_extractor:
    def __init__(self):
        self.templates = {
            'sub':'выч\w{2,}\s+\d+\s*из\s*\d+',
            'search_1':'найди\s\w*',
            'search_2':'--',
            'search_3':'--',
            'task_manager':'открой\sдиспетчер\sзадач',
            'system_settings':'открой\sпанель\sуправления',
            'close':'закр\w*',
            'new_tab':'открой\sбраузер',
            'enable_sound':'включи\sзвук',
            'disable_sound':'выключи\sзвук'
        }
        self.feature_funcs = {
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
    
    def find_command(self, text):
        text = text.lower()
        for key in self.templates.keys():
            match = re.match(self.templates[key],text)
            if match:
                return (key, match.group())
        return (False, False)
    
    def extract_features(self, key, text):
        return self.feature_funcs[key](text)
    
    def _sub_func(self, text):
        features = text.split(' ')
        return (float(features[-1]), float(features[-3]))
    
    def _search_func_1(self, text):
        return text.split(' ')[1:]
    
    def _webbrowser(self, text):
        return ''
    
    def _taskmgr(self, text):
        return ''
    
    def _control(self, text):
        return ''
    
    def _close(self, text):
        return ''
    
    def _enable_sound(self, text):
        return ''
    
    def _disable_sound(self, text):
        return ''