import re

class Command_extractor:
    def __init__(self):
        self.templates = {
            'sub':'выч\w{2,}\s+\d+\s*из\s*\d+',
            'search_1':'йй',
            'search_2':'йй',
            'search_3':'йй',
           'task_manager':'йй',
           'system_settings':'йй',
            'close':'йй',
            'new_tab':'открой\sбраузер',
            'enable/disable_sound':'йй'
        }
        self.feature_funcs = {
            'sub':self._sub_func,
            'search_1':'',
            'search_2':'',
            'search_3':'',
            'task_manager':'',
            'system_settings':'',
            'close':'',
            'new_tab':self._webbrowser,
            'enable/disable_sound':''
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
    
    def _webbrowser(self, test):
        return ''
