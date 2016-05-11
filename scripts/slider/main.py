from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

#Window sizeの設定
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(padding=50)

        self.label=Label(text="Please slide the slider")
        self.add_widget(self.label)

        self.slider = Slider(min=-100, max=100, value=25)
        self.slider.bind(value=self.callback)
        self.add_widget(self.slider)

    def callback(self,instance,value):
        self.label.text=str(value)

class TestApp(App):
    def build(self):
        self.root = root = RootWidget()
        self.title = 'Slider Sample'
        return self.root

TestApp().run()
