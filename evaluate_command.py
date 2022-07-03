import webbrowser

class Command_evaluator():
    def __init__(self):
        self.comm_to_func = {
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
    
    def evaluate(self, key, features):
        return self.comm_to_func[key](features)
    
    def _sub_func(self, features):
        return str(features[0] - features[1])
    
    def _webbrowser(self, features):
        webbrowser.open('https://www.google.com/')
        return 'Исполнено!'
