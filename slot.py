from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.textinput import TextInput
from kivy.properties import *
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import FadeTransition

from realbutton import RealToggleButton
from kivy.uix.slider import Slider

from kivy.uix.gridlayout import GridLayout

class Slot(FloatLayout):

    logic = ObjectProperty(None)

    number = NumericProperty(0)

    loadbutton = ObjectProperty(None)
    savebutton = ObjectProperty(None)

    label = ObjectProperty(None)

    def __init__(self, number, switchto_main, **kwargs):
       super(Slot, self).__init__(**kwargs)
       self.logic = App.get_running_app().logic
       self.number = number
       self.build_interface()
       self.switchto_main = switchto_main

    def update_label(self, newtext):
        self.label.text = newtext

    def save(self, instance):
        App.get_running_app().save_game(slot = self.number)
        self.parent.parent.parent.update_saves()

    def load(self, instance):
        App.get_running_app().load_game(slot = self.number)
        self.switchto_main(self)

    def build_interface(self):
        self.label = Label(
            text = 'Slot: {}'.format(self.number),
            size_hint = (0.5, 1),
            pos_hint = {'x' : 0, 'y' : 0}            
        )
        self.loadbutton = Button(
            text = 'Load',
            size_hint = (0.25, 1),
            pos_hint = {'x' : 0.5, 'y' : 0},
            on_press = self.load
        )

        self.savebutton = Button(
            text = 'Save',
            size_hint = (0.25, 1),
            pos_hint = {'x' : 0.75, 'y' : 0},
            on_press = self.save
        )

        self.add_widget(self.label)
        self.add_widget(self.loadbutton)
        self.add_widget(self.savebutton)

#class SettingsSlot(FloatLayout):
class SettingsSlot(GridLayout):

    logic = ObjectProperty(None)

    label = ObjectProperty(None)
    changer = ObjectProperty(None)

    value = ObjectProperty(None)

    def __init__(self, **kwargs):
       super(SettingsSlot, self).__init__(**kwargs)

       self.setting_value = kwargs.get('setting_value')
       self.setting_min = kwargs.get('setting_min')
       self.setting_max = kwargs.get('setting_max')
       self.setting_type = kwargs.get('setting_type')

       self.label_text = kwargs.get('label_text')

       self.rows = 1

       #self.value = None

       self.build_interface()

    def on_value(self, instance, value):

        if self.setting_type == 'number':
            self.changer.value = value
        elif self.setting_type == 'bool':
            self.changer.pressed = value
            if not value:
                self.changer.source = self.changer.realtexture
                self.changer.reload()
            else:
                self.changer.source = self.changer.realtexture_pressed
                self.changer.reload()

    def build_interface(self):
        self.label = Label(
            text = self.label_text,
        )

        if self.setting_type == 'number':
            self.changer = Slider(
                min = self.setting_min,
                max = self.setting_max,
                value = self.setting_value,
            )
            self.changer.bind(value = self.change_value)
        elif self.setting_type == 'bool':
            self.changer = RealToggleButton(
                './media/icons/settings.png',
                './media/icons/settings_pressed.png',
                self.change_value,
                source = './media/icons/settings.png',
                always_release = True
            )

        self.add_widget(self.label)
        self.add_widget(self.changer)

    def change_value(self, instance, value=0):
        if self.setting_type == 'number':
            self.value = value
        elif self.setting_type == 'bool':
            self.value = not self.changer.pressed
