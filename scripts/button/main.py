#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(cols=2)

        self.btn1=Button(text="Btn1",size_hint = (0.5, 0.5))
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        layout.add_widget(self.btn1)
        self.add_widget(layout)

        self.btn2=Button(text="Btn2",size_hint = (0.5, 0.5))
        layout2 = AnchorLayout(anchor_x='center', anchor_y='center')
        layout2.add_widget(self.btn2)
        self.add_widget(layout2)

        self.btn3=Button(text="Btn3",size_hint = (0.5, 0.5))
        layout3 = AnchorLayout(anchor_x='center', anchor_y='center')
        layout3.add_widget(self.btn3)
        self.add_widget(layout3)

        self.btn4=Button(text="Btn4",size_hint = (0.5, 0.5))
        layout4 = AnchorLayout(anchor_x='center', anchor_y='center')
        layout4.add_widget(self.btn4)
        self.add_widget(layout4)
 
    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')
       
class TestApp(App):
    def build(self):
        self.root = RootWidget()
        self.title = 'Text Input Sample'
        return self.root

TestApp().run()
