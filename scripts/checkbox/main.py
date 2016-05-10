#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
Window.clearcolor = (0.7, 0.7, 0.7, 0.7)

class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(cols=2)

        self.label=Label(text="Check 1")
        self.add_widget(self.label)

        self.checkbox = CheckBox()
        self.checkbox.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox)

        self.label=Label(text="Check 2")
        self.add_widget(self.label)

        checkbox1 = CheckBox()
        self.add_widget(checkbox1)

        self.label=Label(text="Check 3")
        self.add_widget(self.label)

        checkbox3 = CheckBox()
        self.add_widget(checkbox3)
 
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
