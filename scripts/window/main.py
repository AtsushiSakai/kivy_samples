from kivy.app import App
from kivy.uix.button import Label
from kivy.config import Config

#Window sizeの設定
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class TestApp(App):
    def build(self):
        self.title = 'Window Sample'
        self.icon = 'images.jpg'
        return Label(text='Hello World')

TestApp().run()
