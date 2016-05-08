from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.actionbar import ActionBar, ActionItem, ActionButton, ActionView, ActionPrevious, ActionGroup
from kivy.uix.floatlayout import FloatLayout

#Window sizeの設定
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class MyActionBar():
    def __init__(self):

        actionview = ActionView()
        actionview.use_separator=True
        ap = ActionPrevious(title='Action Bar', with_previous=False) 
        actionview.add_widget(ap) 
        self.abtn1=ActionButton(text="Btn1")
        self.abtn1.bind(on_press=self.ActionBtn1Callback)
        actionview.add_widget(self.abtn1) 
        self.abtn2=ActionButton(text="Btn2")
        self.abtn2.bind(on_press=self.ActionBtn2Callback)
        actionview.add_widget(self.abtn2) 

        self.abtn3=ActionButton(text="Btn3",icon="images.jpg")
        self.abtn3.bind(on_press=self.ActionBtn3Callback)
        actionview.add_widget(self.abtn3) 

        group1=ActionGroup()

        self.abtn4=ActionButton(text="Btn4")
        self.abtn4.bind(on_press=self.ActionBtn4Callback)
        group1.add_widget(self.abtn4)

        self.abtn5=ActionButton(text="Press Me!!!!")
        self.abtn5.bind(on_press=self.ActionBtn5Callback)
        group1.add_widget(self.abtn5)



        actionview.add_widget(group1)

        self.actionbar=ActionBar()
        self.actionbar.add_widget(actionview)


    def ActionBtn1Callback(self,instance):
        print("Btn1 press!!")

    def ActionBtn2Callback(self,instance):
        print("Btn2 press!!")

    def ActionBtn3Callback(self,instance):
        print("Btn3 press!!")

    def ActionBtn4Callback(self,instance):
        print("Btn4 press!!")

    def ActionBtn5Callback(self,instance):
        print("Btn5 press!!")


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World",
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5}))

        self.myactionbar=MyActionBar()

        self.add_widget(
            self.myactionbar.actionbar
            )



class TestApp(App):
    def build(self):
        self.root = root = RootWidget()
        self.title = 'Window Sample'
        self.icon = 'images.jpg'
        return self.root

TestApp().run()
