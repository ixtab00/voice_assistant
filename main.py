import audio_to_text
import extract_command
import evaluate_command
import tkinter

class App():
    SIZE = "300x300"
    NAME = 'Voice Assistant'
    def __init__(self):
        self.recognizer = audio_to_text.SpeechToText()
        self.extractor = extract_command.Command_extractor()
        self.evaluator = evaluate_command.Command_evaluator()
        self.win = tkinter.Tk()
        self.win.title(App.NAME)
        self.win.geometry(App.SIZE)
        self.voice_bttn = tkinter.Button(self.win, text='Командуй!', command=self.start_pipeline)
        self.voice_bttn.place(height = 25, width = 100,x = 100, y = 15)
        self.command_label = tkinter.Label(self.win, text = "Ваша команда", justify=tkinter.LEFT)
        self.command_label.place(height=15, x = 50, y = 80)
        self.text_output = tkinter.Text(self.win, background='#999')
        self.res_label = tkinter.Label(self.win, text = "Результат", justify=tkinter.LEFT)
        self.res_label.place(height=15, x = 50, y = 130)    
        self.text_output.place(height = 100, width = 200, x = 50, y = 150)
        self.command = tkinter.Text(self.win, background='#999')
        self.command.place(height = 25, width = 200, x = 50, y = 100)


    def start_pipeline(self):
        with self.recognizer.micro as source:
            audio = self.recognizer.recognizer.listen(source, 2, 5)
            text = self.recognizer.get_text(audio)
            self.command.delete(1.0, tkinter.END)
            self.command.insert(tkinter.INSERT, text)
        key, comm = self.extractor.find_command(text)
        if key:
            features = self.extractor.extract_features(key, comm)
            res = self.evaluator.evaluate(key, features)
        else:
            res = 'Неизвестная команда'
        self.text_output.delete(1.0, tkinter.END)
        if res:
            self.text_output.insert(tkinter.INSERT, res)
        else:
            self.text_output.insert(tkinter.INSERT, 'Команда не выполнена.')

    def mainloop(self):
        self.win.mainloop()

app = App()
app.mainloop()